import logging
import os
import unittest
from tempfile import gettempdir

from reactome_analysis_worker.geneset_builder import fetch_reactome_geneset, load_reactome_interactors, load_reactome_disease_pathways
from reactome_analysis_worker.models.gene_set import GeneSet


class TestCreateReactomeGenesets(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

    def test_build_from_file(self):
        source = os.path.join(os.path.dirname(__file__), "testfiles")

        gene_set = fetch_reactome_geneset(source=source, species="Homo sapiens")

        self.assertTrue("R-HSA-2029481" in gene_set.gene_sets)
        self.assertEqual(4, len(gene_set.gene_sets["R-HSA-2029481"]))

        # make sure there is a name for every pathway
        for gene_set_id in gene_set.gene_sets:
            self.assertIsNotNone(gene_set.gene_set_names[gene_set_id])

    def test_build_from_url(self):
        source = "https://reactome.org/download/current"

        gene_set = fetch_reactome_geneset(source=source, species="Homo sapiens")

        self.assertTrue("R-HSA-1980143" in gene_set.gene_sets)
        self.assertEqual(150, len(gene_set.gene_sets["R-HSA-1980143"]))

    def test_load_interactors(self):
        filename = os.path.join(os.path.dirname(__file__), "testfiles", "IntAct_Static_100.txt")

        interactors = load_reactome_interactors(filename)

        self.assertEqual(43, len(interactors))
        self.assertTrue("P23497" in interactors)
        self.assertTrue("Q9UKL3" in interactors["P23497"])
        self.assertEqual(23, len(interactors["P23497"]))

    def test_add_gene_set_interactors(self):
        source = os.path.join(os.path.dirname(__file__), "testfiles")
        gene_set = fetch_reactome_geneset(source=source, species="Homo sapiens")
        filename = os.path.join(os.path.dirname(__file__), "testfiles", "IntAct_Static_100.txt")
        interactors = load_reactome_interactors(filename)

        org_gene_set = gene_set.copy()
        gene_set.add_interactors(interactors)

        # no change detectable with test files
        self.assertEqual(len(gene_set.gene_sets["R-HSA-2029481"]), len(org_gene_set.gene_sets["R-HSA-2029481"]))

    def test_load_save(self):
        source = os.path.join(os.path.dirname(__file__), "testfiles")
        gene_set = fetch_reactome_geneset(source=source, species="Homo sapiens")

        filename = os.path.join(gettempdir(), "reactome_human.pikl")

        if os.path.isfile(filename):
            os.unlink(filename)

        gene_set.save(filename)

        loaded_set = GeneSet.create_from_file(filename)

        self.assertEqual(len(gene_set.gene_sets), len(loaded_set.gene_sets))
        self.assertEqual(len(gene_set.gene_set_names), len(loaded_set.gene_set_names))

    def test_load_disease(self):
        url = "https://dev.reactome.org/download/current/HumanDiseasePathways.txt"

        disease_pathways = load_reactome_disease_pathways(url)

        self.assertTrue(isinstance(disease_pathways, list))
        self.assertEqual(516, len(disease_pathways))
        self.assertEqual("R-HSA-1222387", disease_pathways[0])
        self.assertEqual("R-HSA-9665251", disease_pathways[-1])

    def test_remove_pathway(self):
        source = os.path.join(os.path.dirname(__file__), "testfiles")
        gene_set = fetch_reactome_geneset(source=source, species="Homo sapiens")

        org_count = len(gene_set.gene_sets)
        gene_set.remove_pathways(["R-HSA-2029481"])
        self.assertEqual(org_count - 1, len(gene_set.gene_sets))
