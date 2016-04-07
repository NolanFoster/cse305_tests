(* tester.sml *)
use "sml/hw3.sml";
val args = CommandLine.arguments()
val _ = hw3(List.nth (args, 0), List.nth (args, 1))
val _ = OS.Process.exit(OS.Process.success)
