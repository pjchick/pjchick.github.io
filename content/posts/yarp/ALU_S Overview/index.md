---
title: "ALU_S Shift Unit"
date: 2026-02-10
draft: false
description: "Overview of the ALU_S Shifting Unit "
tags: ["ALU", "ALU-Shift"]
---

![ALU_S Design](./images/ALU_S.png)

The ALU Shift card is relatively straight forward. I've expanded the origional H.P. design which only had Shift left into a full featured Shift card.

- Shift Left from B
- Rotate Left from B
- Shift Right from B
- Rotate Right from B

- Shift Left from C
- Rotate Left from C
- Shift Right from C
- Rotate Right from C

Looking at the diagram it's quite straight forward. REgister selection is performed by the Blue relays at the top. Shilf Left or right is controlled by the Red relays and finally the data is gated onto the Data bus via the Green relays. The Grey relay on the right controls the Shift or Rotate function.

The instruction set for the computer is always split into three nibbles the most significan nibble is the op-code. The middle nibble as shown on the diagram is for the source - in this case a shift operation. The last nibble is for the destination register.



