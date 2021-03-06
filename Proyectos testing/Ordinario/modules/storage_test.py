import unittest
import mysql.connector
from unittest.mock import Mock, MagicMock, patch
from trivia import *
from storage import *

class StorageTest(unittest.TestCase):
	def __patch_all(self, mock, **replace):
		e_connect = replace.get("e_connect")
		e_cursor = replace.get("e_cursor")
		rowcount = replace.get("rowcount", 1)
		fetchone = replace.get("fetchone", (None,))
		fetchall = replace.get("fetchall", [])


		# patch all mysql-connector methods (correct values)
		mock.return_value = MagicMock(
			commit = MagicMock(return_value = None),
			close = MagicMock(return_value = None),
			cursor = MagicMock(
				return_value = MagicMock(
					execute = MagicMock(return_value = None),
					close = MagicMock(return_value = None),
					rowcount = rowcount,
					fetchone = MagicMock(return_value = fetchone),
					fetchall = MagicMock(return_value = fetchall)
				)
			)
		)

		# raise errors
		if e_connect:
			mock.side_effect = MagicMock(side_effect = e_connect)

		if e_cursor:
			mock.return_value.cursor.side_effect = MagicMock(side_effect = e_cursor)

	def __test_load_error(self, mock, test_callback, db_raises_tests = True):
		if db_raises_tests:
			tests = [
				{ "e_cursor": mysql.connector.Error() },
				{ "e_connect": mysql.connector.Error() }
			]
		else:
			tests = [{}]

		for t in tests:
			self.__patch_all(mock, **t)
			storage = MyStorage()

			test_callback( # call the callback for testing
				storage,
				t
			)

	def __test_save_error(self, method_name, param, mock, db_raises_tests = True):
		if db_raises_tests:
			tests = [
				{ "e_cursor": mysql.connector.Error() },
				{ "e_connect": mysql.connector.Error() },
				{ "rowcount": 0 }
			]
		else:
			tests = [{}]

		for t in tests:
			self.__patch_all(mock, **t)

			storage = MyStorage()
			output = getattr(storage, method_name)(param)

			self.assertFalse(output)
			

	@patch("mysql.connector.connect")
	def test_save_player(self, mock):
		self.__patch_all(mock)

		# dummy player input
		storage = MyStorage()
		output = storage.save_player(Player("", 2))
		
		self.assertTrue(output)

	@patch("mysql.connector.connect")
	def test_save_player_raises(self, mock):
		self.__test_save_error("save_player", Player("", 1), mock)

	@patch("mysql.connector.connect")
	def test_save_match(self, mock):
		matchs = [
			Match([], Category("")),
			Match([], Category("", 1), Difficulty.medium)
		]

		for m in matchs:
			self.__patch_all(mock) # patch all methods

			m.player = Player("", 1) # dummy player
			storage = MyStorage()
			output = storage.save_match(m)

			self.assertTrue(output)
			

	@patch("mysql.connector.connect")
	def test_save_match_raises(self, mock):
		# dummy input
		match = Match([], Category("", 1))
		match.player = Player("", 1)

		self.__test_save_error("save_match", match, mock)

	@patch("mysql.connector.connect")
	def test_save_match_without_player(self, mock):
		self.__test_save_error("save_match", Match([], Category("", 1)), mock, False)

	@patch("mysql.connector.connect")
	def test_load_players_raises(self, mock):
		def test(storage, test):
			output = storage.load_players()
			self.assertCountEqual(output, [])
		
		self.__test_load_error(
			mock,
			test,
			True
		)

	@patch("mysql.connector.connect")
	def test_load_categories_raises(self, mock):
		def test(storage, test):
			output = storage.load_categories()
			self.assertCountEqual(output, [])
		
		self.__test_load_error(
			mock,
			test,
			True
		)

	@patch("mysql.connector.connect")
	def test_load_player_statistics(self, mock):
		def test(storage, test):
			output = storage.load_player_statistics(Player(""))
			self.assertIsNone(output)
		
		self.__test_load_error(
			mock,
			test,
			True
		)
		

if __name__ == "__main__":
	unittest.main()