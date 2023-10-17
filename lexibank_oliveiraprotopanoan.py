from collections import defaultdict
import pathlib
import attr
from clldutils.misc import slug
from clldutils.markup import add_markdown_text
from lingpy import Wordlist
from pylexibank import Dataset as BaseDataset
from pylexibank import progressbar as pb
from pylexibank import Language, Lexeme, Concept
from pylexibank import FormSpec
from pyedictor import fetch


def unmerge(sequence):
    out = []
    for tok in sequence:
        out += tok.split('.')

    return out


@attr.s
class CustomLanguage(Language):
    NameInSource = attr.ib(default=None)
    Sources = attr.ib(default=None)


@attr.s
class CustomConcept(Concept):
    Proto_Concept = attr.ib(default=None)
    Proto_ID = attr.ib(default=None)
    Original_Concept = attr.ib(default=None)


@attr.s
class CustomLexeme(Lexeme):
    Alignment = attr.ib(default=None)
    Morphemes = attr.ib(default=None)
    UncertainCognacy = attr.ib(default=None)
    ConceptInSource = attr.ib(default=None)
    ProtoSet = attr.ib(default=None)
    EntryInSource = attr.ib(default=None)
    GroupedSounds = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "oliveiraprotopanoan"
    language_class = CustomLanguage
    concept_class = CustomConcept
    lexeme_class = CustomLexeme
    form_spec = FormSpec(
            separators="~;,/",
            missing_data=["--", "- -", "-", "-- **", "--.", "- --"],
            replacements=[(" ", "_")],
            first_form_only=True
            )

    def cmd_readme(self, args):
        return add_markdown_text(BaseDataset.cmd_readme(self, args),
                                 "- the article in which we describe the digitization and creation of alignments: \n  > Blum, Frederic and Barrientos, Carlos. 2023. “A New Dataset with Phonological Reconstructions in CLDF,” in Computer-Assisted Language Comparison in Practice, 21/06/2023, https://calc.hypotheses.org/6142.",
                                 section='How to cite')

    def cmd_download(self, _):
        print("updating ...")
        with open(self.raw_dir.joinpath("raw.tsv"), "w", encoding="utf-8") as f:
            f.write(
                fetch(
                    "oliveiraprotopanoan",
                    columns=[
                        "ALIGNMENT",
                        "COGID",
                        "COGIDS",
                        "CONCEPT",
                        "DOCULECT",
                        "FORM",
                        "VALUE",
                        "TOKENS",
                        "MORPHEMES",
                        "COMMENT",
                        "SOURCE",
                        "PROTO_SET",
                        "ENTRY_IN_SOURCE",
                        "CONCEPT_IN_SOURCE",
                        "UNCERTAIN_COGNACY"
                    ],
                )
            )

    def cmd_makecldf(self, args):
        args.writer.add_sources()
        args.log.info("added sources")

        # add conceptlists
        concepts = defaultdict()
        proto_concepts = defaultdict()

        # Proto Concepts: New
        proto_list = self.etc_dir.read_csv(
            "proto_concepts.tsv",
            delimiter="\t",
            dicts=True
            )

        for e, concept in enumerate(proto_list):
            idx = str(e) + "_" + slug(concept["GLOSS"])
            args.writer.add_concept(
                ID=idx,
                Name=concept["ENGLISH"],
                Original_Concept=concept["GLOSS"],
                Concepticon_ID=concept["CONCEPTICON_ID"],
                Concepticon_Gloss=concept["CONCEPTICON_GLOSS"],
                Proto_ID=concept["PROTO_ID"]
                )

            concepts[concept["ENGLISH"]] = idx
            proto_concepts[concept["PROTO_ID"]] = concept["ENGLISH"]

        # Other Concepts
        other_concepts = self.etc_dir.read_csv(
            "other_concepts.tsv",
            delimiter="\t",
            dicts=True
            )

        for e, concept in enumerate(other_concepts):
            idx = str(e) + "_" + slug(concept["GLOSS"])
            args.writer.add_concept(
                ID=idx,
                Original_Concept=concept["GLOSS"],
                Name=proto_concepts[concept["PROTO_ID"]],
                Proto_ID=concept["PROTO_ID"],
                Proto_Concept=concept["PROTO_CONCEPT"]
                )
            concepts[concept["GLOSS"]] = idx

        args.log.info("added concepts")

        # add language
        languages = {}
        sources = defaultdict()
        for language in self.languages:
            args.writer.add_language(
                    ID=language["ID"],
                    Name=language["Name"],
                    Glottocode=language["Glottocode"]
                    )
            languages[language["ID"]] = language["Name"]
            sources[language["ID"]] = language["Sources"]
        args.log.info("added languages")

        data = Wordlist(str(self.raw_dir.joinpath("raw.tsv")))

        # add data
        for (
            idx,
            alignment,
            cogid,
            concept,
            language,
            form,
            value,
            tokens,
            morphemes,
            comment,
            source,
            proto_set,
            entry_in_source,
            concept_in_source,
            uncertain_cognacy
        ) in pb(
            data.iter_rows(
                "alignment",
                "cogid",
                "concept",
                "doculect",
                "form",
                "value",
                "tokens",
                "morphemes",
                "comment",
                "source",
                "proto_set",
                "entry_in_source",
                "concept_in_source",
                "uncertain_cognacy"
            ),
            desc="cldfify"
        ):
            lexeme = args.writer.add_form_with_segments(
                Parameter_ID=concepts[concept],
                Language_ID=language,
                Form=form.strip(),
                Value=value.strip() or form.strip(),
                Segments=unmerge(tokens),
                GroupedSounds=tokens,
                Source="Oliveira2014" if source == "" else source,
                Cognacy=cogid,
                Alignment=" ".join(alignment),
                Morphemes=morphemes,
                Comment=comment,
                ProtoSet=proto_set,
                ConceptInSource=concept_in_source,
                EntryInSource=entry_in_source,
                UncertainCognacy=uncertain_cognacy,
            )

            args.writer.add_cognate(
                lexeme=lexeme,
                Cognateset_ID=cogid,
                Source=source
                )
