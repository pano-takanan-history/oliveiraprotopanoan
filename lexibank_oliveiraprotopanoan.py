import attr
from collections import defaultdict
import pathlib
from clldutils.misc import slug
from pylexibank import Dataset as BaseDataset
from pylexibank import progressbar as pb
from pylexibank import Language, Lexeme, Concept
from pylexibank import FormSpec


@attr.s
class CustomLanguage(Language):
    NameInSource = attr.ib(default=None)
    Sources = attr.ib(default=None)


@attr.s
class CustomConcept(Concept):
    Spanish_Gloss = attr.ib(default=None)


@attr.s
class CustomLexeme(Lexeme):
    UncertainCognacy = attr.ib(default=None)
    Concept_From_Proto = attr.ib(default=None)
    Paragraph = attr.ib(default=None)
    Source = attr.ib(default=None)
    EntryInSource = attr.ib(default=None)
    Variants = attr.ib(default=None)


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

    def cmd_makecldf(self, args):
        # add bib
        args.writer.add_sources()
        args.log.info("added sources")

        # Add replacement table for sources
        rep_table = self.raw_dir.read_csv(
            "source_replacements.tsv", delimiter="\t", dicts=True
        )
        sources = defaultdict()
        for source in rep_table:
            sources[source["old"]] = source["new"]

        # add concept
        concepts = {}
        for concept in self.concepts:
            idx = slug(concept["SPANISH"])
            args.writer.add_concept(
                    ID=idx,
                    Name=concept["SPANISH"],  # TODO must be translated to ENGLISH later!
                    Spanish_Gloss=concept["SPANISH"],
                    Concepticon_ID=concept["CONCEPTICON_ID"],
                    Concepticon_Gloss=concept["CONCEPTICON_GLOSS"]
                    )
            concepts[concept["SPANISH"]] = idx
        args.log.info("added concepts")

        # add language
        languages = args.writer.add_languages(lookup_factory="NameInSource")
        args.log.info("added languages")

        # read in data
        data = self.raw_dir.read_csv(
            "parsed-entries2.tsv", delimiter="\t", dicts=True
        )

        # add data
        for entry in pb(data, desc="cldfify", total=len(data)):
            if " [" in entry["VALUE"]:
                phon = entry["VALUE"].split(" [")[1:]
                value = phon[0].strip("] ~")
                variants = (str(phon[1]).strip("] ~") if len(phon) > 1 else "")
                # print(variants)

            else:
                value = entry["VALUE"]
                variants = ""

            for lexeme in args.writer.add_forms_from_value(
                    Language_ID=languages[entry["DOCULECTID"]],
                    Parameter_ID=concepts[entry["CONCEPT"].strip()],
                    Value=value,
                    Concept_From_Proto=entry["CONCEPT_FROM_PROTO"],
                    Variants=variants,
                    Comment=entry["NOTE"],
                    Source=entry["SOURCE"],
                    UncertainCognacy=entry["VALUE_UNCERTAIN"],
                    Paragraph=entry["IDX"],
                    Cognacy=entry["IDX"][1:],
                    EntryInSource=entry["ENTRY_IN_SOURCE"],
                    ):
                args.writer.add_cognate(
                        lexeme=lexeme,
                        Cognateset_ID=entry["IDX"][1:],
                        Cognate_Detection_Method="expert",
                        Source="Oliveira2014"
                        )
