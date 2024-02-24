from src.etl.patterns.orchestrator import Orchestrator
import src.etl.refining.engine as mrn


class RefinerOrchestrator(Orchestrator):

	def __init__(self):
		super().__init__()

		self.process = "REFINING"

		# Path formation
		## Cleaned Paths
		# self.clnd_mrn_cold_path	= self.paths.get_file_path("cleaned",   "mrn_cleaned_cold.parquet")
		self.clnd_mrn_hot_path	= self.paths.get_file_path("cleaned",   "mrn_cleaned_hot.parquet")
		# self.clnd_night_path	= self.paths.get_file_path("cleaned",   "ngt_cleaned.parquet")
		# self.clnd_morning_path = self.paths.get_file_path("cleaned", "mrn_cleaned.parquet")
		self.rfnd_weight_path  = self.paths.get_file_path("refined", "WM_WeightMeasurements.parquet")

		# Define tables_relation list
		self.tables_relation = [
			["weight", self.clnd_mrn_hot_path, self.rfnd_weight_path]
		]

		# Create an instance of RefiningFunctions for executing refinements
		self.refining_functions = mrn.RefiningFunctions()

	def execute(self):
		self.logger = Orchestrator.logger
		for refine_id, cleaned_path, refined_path in self.tables_relation:
			self.logger.info("*********************************************************")
			self.logger.info(f"///////// STARTING {refine_id} REFINING PROCESS /////////")
			self.logger.info("*********************************************************")
			
			cleaned_data = self.reading(file_format="parquet", file_path=cleaned_path)
			
			refined_data = self.refining_functions.refine(df_cleaned=cleaned_data, refine_id=refine_id)
			
			self.writing(df_to_write=refined_data, file_path=refined_path)
