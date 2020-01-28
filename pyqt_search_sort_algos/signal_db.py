from ensegilib.parserlib.src.measurementparsers.mdfparser import MdfParser
from utils import timing


class Persistance():
	def __init__(self, mdf_filepath):
		self.signal_dict = {}
		self.mdf_parser = MdfParser(mdf_filepath)

	@timing
	def get_all_signals(self):
		signal_group = None
		for group in self.mdf_parser.mdf_object.groups:
			signals = group.channels
			for signal in signals:
				if signal.source is not None:
					signal_group = signal.source.name
				rsignal=self.mdf_parser.mdf_object.get(signal.name, raw = True)
				self.signal_dict[signal.name] = (signal_group, rsignal.unit,)

