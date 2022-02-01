

define char = Character(name = None, show_two_window=True)


define narrator = nvl_narrator #(ctc="ctc", ctc_pause="ctc", ctc_position="nestled")
define Thought = Character(" ", ctc="ctc", ctc_pause="ctc", ctc_position="fixed")
define Thought2 = Character(" ", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind=nvl)


define Fuuji = Character("Nakamura", color="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Kikuchiyo = Character("Kikuchiyo", color="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Akane = Character("Akane", color="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)


define Student = Character("Student", color ="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Princess = Character(" ? ? ? ", color="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Dad = Character("Dad", color="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Mom = Character("Mom", color="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Man = Character("Man", color="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Girl = Character("Girl", color="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Applicant = Character("Applicant", color ="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)
define Shinazu = Character("Shinazu",color ="fff", ctc="ctc", ctc_pause="ctc", ctc_position="fixed", kind = char)