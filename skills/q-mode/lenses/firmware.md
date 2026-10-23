# Lens: firmware

## Artifact identity
Firmware image hash, bootloader version, configuration, hardware revision of the target, and unit serials. Record them for every run.

## Stimulus and observation
Inputs on pins and buses (UART, I²C, SPI, CAN, BLE, Wi-Fi), controlled power and reset, simulated sensors, network traffic. Observe console and log output, bus traces, current draw, GPIO states, radio behavior, and persistent storage.

## Instruments and trust
Simulators, the HIL rig, power supplies and relays, logic analyzers, current probes. Run a doctor check before each campaign: controller firmware, connections, power state. Keep a known-good unit for comparison.

## Variation and sampling
Unit-to-unit differences, temperature, supply voltage, radio conditions, timing at worst-case load. Test across units and corners. Repeat timing-sensitive faults many times, because the window that bricks a device is narrow.

## Cost and reversibility
Rig time is scarce. Bricking a prototype, burning eFuses or OTP, locking debug ports, and writing identity or calibration data cannot be undone. Each needs the operator's yes per unit. The guard hook asks before common commands of this kind.

## Oracle sources
Interface and protocol specifications, datasheets, timing budgets, power budgets, and the product requirements.

## Gates and standards
Merge (host and simulation tests), pre-release (HIL), field rollout in stages. Safety-related firmware adds the regulated lens.

## Layer ladder
Host unit tests → model-in-the-loop → software-in-the-loop → processor-in-the-loop → hardware-in-the-loop → system on real units → field telemetry. A build that only compiled verified the toolchain, not the product.

## Typical risks
- **Boot and recovery:** cold and warm boot, brownout, watchdog reset, hang detection, boot loops, safe mode.
- **Update path:** interrupted download, power loss at every phase of write and swap, corrupted or wrongly signed image, wrong-hardware image, failed health check triggering rollback, rollback with no valid previous image, downgrade protection.
- **Resources:** stack and heap headroom, flash wear, fragmentation over long runs, CPU load, interrupt latency at worst case.
- **Timing and concurrency:** deadlines, ISR and task interaction, priority inversion, clock drift.
- **Power:** sleep and wake, current per mode, behavior at supply limits.
- **Interfaces:** malformed and out-of-range input, bus errors, unplug and replug, radio loss and reconnection.
- **Persistent state:** settings and calibration surviving updates and power loss, factory reset.
- **Security:** secure boot, debug port state in production, key storage, signed updates.

## Failure classes
Rig or fixture fault, unit defect, build or configuration mismatch (wrong image on the unit), and marginal hardware showing up as firmware flakiness.

## Playbook notes
- **Test campaign:** fault injection on the rig (random power cuts, brownouts, sensor open and short, bus noise, dropped packets) and soak runs with duration and conditions reported.
- **Flaky triage:** log temperature, voltage, unit serial, and fixture with every run.
