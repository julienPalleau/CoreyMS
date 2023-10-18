from unittest import TestCase
from printer import Printer, PrinterError


class TestPrinter(TestCase):
    # here you run a new printer for each test you are doing
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    # if you wish to run the same printer only once for all the tests then you have to replace the above lines as follow:
    # This is usually not good to do that as you introduce dependency between tests i.e first test you print 30 pages,
    # if during your second test you try to print 272 pages it will fail because you run out of paper not because
    # something is wrong. So it is better to start with a fresh new printer for each new test.
    # @classmethod
    # def setUp(cls) -> None:
    #     cls.printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        message = self.printer.print(25)

    def test_print_outside_cpacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."

        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = "Printed 11 pages in 3.67 seconds."
        result = fast_printer.print(pages)
        self.assertEqual(result, expected)

    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

    def test_multiple_runs_end_up_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

        with self.assertRaises(PrinterError):
            self.printer.print(1)
