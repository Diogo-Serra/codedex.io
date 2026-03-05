#!/usr/bin/env python3

notes = {
    261: "C4",
    294: "D4",
    329: "E4",
    349: "F4",
    392: "G4",
    440: "A4",
    494: "B4",
    523: "C5",
    0:   "REST",
}


def altair_to_notes(switches):
    return [notes[int(s, 2)] for s in switches]
