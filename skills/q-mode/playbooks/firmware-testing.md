### Firmware testing

**You own confidence in code that runs on hardware. Simulate what you can, then prove the rest on real units.**

For embedded firmware, device drivers, bootloaders, and anything flashed onto a device.

1. Pin identity: firmware image hash, bootloader version, configuration, hardware revision, and unit serials for every run. A result without identities is `INCONCLUSIVE`.
2. Layer the tests (**principle-cheapest-layer-that-catches-it**): host unit tests for logic, model-in-the-loop and software-in-the-loop for control and protocol behavior, processor-in-the-loop for timing on the target, and hardware-in-the-loop on a rig for peripherals, power, and physical I/O. A green build that only compiled has verified the toolchain, not the product.
3. Cover the firmware-specific risks:
   - **Boot and recovery:** cold and warm boot, brownout, watchdog reset, hang detection, boot loops, and safe mode.
   - **Update path:** interrupted download, power loss at every phase of write and swap, corrupted or wrongly signed image, wrong-hardware image, health-check failure triggering rollback, rollback with no valid previous image, and downgrade protection.
   - **Resources:** stack and heap headroom, flash wear, memory fragmentation over long runs, CPU load, and interrupt latency at worst case.
   - **Timing and concurrency:** deadlines, ISR and task interaction, priority inversion, and clock drift.
   - **Power:** sleep and wake, current budget per mode, and behavior at supply limits.
   - **Interfaces:** protocol conformance, malformed and out-of-range input, bus errors, unplug and replug, and radio loss and reconnection.
   - **Persistent state:** settings and calibration surviving updates and power loss, and factory reset.
   - **Security:** secure boot, debug port state in production, key storage, and signed updates.
4. Inject faults on the rig where the risk lives: power cuts at random points, brownouts, sensor open and short circuits, bus noise, and dropped packets. Repeat power-loss tests many times, because the window that bricks a device is narrow.
5. Run long: soak tests for leaks, wear, and drift. Report duration and conditions.
6. Check the rig before believing it (**principle-trust-the-instrument**): a doctor check, a known-good unit, and controlled power and reset.
7. Irreversible operations (fuses, OTP, debug lock, identity writes) need the operator's yes per unit (**principle-protect-shared-environments**).

**Reply:** the identities tested, results per layer, fault-injection counts and outcomes, soak results with duration, and residual risk.
