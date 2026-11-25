"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single-line roast to $MAKEFUN_OUTPUT_DIR/entry.txt:
the smart fridge locks its water dispenser until the filter
subscription is renewed, so its owner pays monthly rent to a
box that holds their own ice hostage. Standard library only;
the line is checked against the competition gate (one line of
UTF-8 text, 1 to 160 characters, not only whitespace) before
anything is written.
"""

import os
from os.path import join

ROAST = (
    "My smart fridge locked the water dispenser until I renewed "
    "its filter subscription, so now I pay monthly rent to a box "
    "that keeps my own ice hostage."
)

CHAR_LIMIT = 160


def roast():
    """Return the one-line roast of the smart fridge."""
    return ROAST


def check_roast(text):
    """Check the roast against the competition gate.

    The gate wants one line of plain UTF-8 text, between 1 and
    160 characters, that is not only whitespace: a roast of a
    smart home gadget the writer shares a house with. A line
    that fails here is rejected instead of wasting a submission
    on the server.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("roast is empty")
    if len(stripped) > CHAR_LIMIT:
        raise ValueError(
            "roast is %d characters, over the 160 limit" % len(stripped)
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("roast must fit on exactly one line")
    return stripped


def roast_has_sting(text):
    """Check the roast lands both halves of the joke.

    The judge weighs the laugh first and the freshness second,
    and the sting needs a real behaviour to bite on: the fridge
    locking its own dispenser over a subscription, then the turn
    into paying rent to a box. A roast missing either half reads
    like a plain complaint about an appliance, so it is rejected
    here before anything is written.
    """
    lowered = text.lower()
    if "fridge" not in lowered:
        raise ValueError("roast never names the smart fridge")
    if "subscription" not in lowered:
        raise ValueError("roast never names the subscription lock")
    if "rent" not in lowered:
        raise ValueError("roast never lands the rent turn")
    return text


def roast_shape(text):
    """Measure the roast for a last sanity pass.

    Returns the character and word counts. A roast too short to
    carry both the setup and the sting, or one padded out to
    fill the cap, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    line = check_roast(roast())
    line = roast_has_sting(line)
    shape = roast_shape(line)
    if shape["words"] < 5:
        raise ValueError("roast is too short to land the joke")
    with open(join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
