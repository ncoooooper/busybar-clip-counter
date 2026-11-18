# Emulator verification

Replayed documented game-state fields through the HTTP event receiver. A live CS2 match was unavailable.

Posted a game event with 17 in the active item's clip and 60 in reserve. The display left standby and showed the active values.

13 distinct frames were recorded on firmware 1.3.1. App io.ncoooooper.clipcounter exited: finished; heap peak 81.8 of 128 KiB. Screenshots are in screenshots/ and the recording is in media/.

## Display capture

Firmware 1.3.1 rendered both README examples. The display run replayed sample inputs in a separate emulator project. The source test above describes how those readings were obtained. Each square in a guide GIF is one front-display pixel enlarged to 9 × 9. The production archive was built from the source in this repository.
