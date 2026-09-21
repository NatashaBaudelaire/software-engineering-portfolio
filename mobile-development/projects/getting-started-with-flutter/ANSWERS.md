# Lesson 02 - Mobile Development (offline)

## Part A

### A1 - Output of `flutter doctor -v`

Summarized output of `flutter doctor -v` run on 19/09/2026 in this environment:

```text
[√] Flutter (Channel stable, 3.47.1, on Microsoft Windows [Version 10.0.26200.9457], locale en-GB)
[√] Windows Version (Windows 11 or higher, 25H2, 2009)
[!] Android toolchain - develop for Android devices (Android SDK version 37.0.0)
    X Android license status unknown.
[X] Chrome - develop for the web (Cannot find Chrome executable at .\Google\Chrome\Application\chrome.exe)
[√] Visual Studio - develop Windows apps (Visual Studio Community 2026 18.9.1)
[√] Connected device (2 available)
[√] Network resources
! Doctor found issues in 2 categories.
```

Of the four required items in this course (Flutter, Android toolchain, Network
resources and Connected device), three are green. **Android toolchain** shows up
as `[!]` because of the license check (see Problem 2), and the Chrome `[X]` does
**not** block the work, because the goal is not to publish to Flutter Web but to
run the app (Edge appears in `flutter devices`).

### A2 - Record of the problems faced

Summary of the real problems encountered in this lesson (detailed in Part D,
Problems 1 to 7): missing Chrome; Android licenses not recognized by
`flutter doctor`; NDK installation via command line; no phone/emulator at the
time of the experiments; transient engine exception on hot restart; the
`flutter run --machine` protocol format; and the isolate id changing after a
restart.

## Part C - Hot Reload and Hot Restart experiments

**Platform observed:** Edge (web), via `flutter run -d edge`. There was no
Android emulator or physical device available in the environment, so the
experiments were done on the web version of the app. The app had the teal theme
and the counter incrementing by 3.

Commands were driven through the `flutter run --machine` protocol (appId
`281d32a6-ffd8-46d7-a9e6-02623a57f93e`). App state was verified by widget tree
dumps (extension `ext.flutter.debugDumpApp`), and rendered colors were read
directly from the canvas pixels (via the Chrome DevTools Protocol).

### C1 - Hot reload preserves state (r)

1. With the app running and the counter at **15** (5 taps), I temporarily changed
   the static text in `lib/main.dart` from `You have pushed the button this many
   times:` to `Experiment C1: changed text`.
2. Trigger: `app.restart` command with `fullRestart: false` (equivalent to `r`).
   Tool response: `Reloaded application in 580ms.` (`result.code: 0`).
3. Widget tree dump after the reload: the displayed text became
   **"Experiment C1: changed text"** and the counter stayed at **15**.
   In other words, hot reload applied the code change **without losing the
   screen state**.
4. Next, I changed the initializer `int _counter = 0;` to `int _counter = 50;`
   (temporary change) and applied hot reload (441 ms): the counter **kept its
   value** because field initializers **are not re-executed** on hot reload;
   the existing state is preserved.
5. Temporary change reverted at the end.

### C2 - Visual change (theme) via Hot Reload

1. I temporarily changed the theme in `lib/main.dart`:
   `ColorScheme.fromSeed(seedColor: Colors.teal)` → `Colors.amber`.
2. Hot reload (`fullRestart: false`), `Reloaded application in 455ms.` (`code: 0`).
3. Actual rendered colors (canvas pixels):

   | Element | Before (teal) | After (amber) |
   |---|---|---|
   | Increment FAB background | `#005048` | `#5b4300` |
   | AppBar background (inversePrimary) | `#82d5c8` | `#e9c16c` |

   The theme change was applied immediately, without closing/reopening the app,
   and the counter kept its previous value - state preserved again.
4. I reverted to `Colors.teal` + hot reload (496 ms) and the colors returned to
   the original.

### C3 - Hot Restart resets state (Shift+R)

1. With the app showing counter **15** (live state), I temporarily changed the
   initializer to `int _counter = 50;` in `lib/main.dart`.
2. Trigger: `app.restart` command with `fullRestart: true` (equivalent to
   `Shift+R`). Response: `Restarted application in 1,515ms.` (`code: 0`). The
   Dart isolate changed its id after the restart (verified in the VM service).
3. Widget tree dump: the counter now shows **50** (the new initial value from the
   code). The previous value (15) was **lost**: hot restart re-runs `main()`
   and rebuilds the state from the code.
4. I reverted to `int _counter = 0;` and applied **hot restart**
   (`Restarted application in 479ms.`): the app showed counter **0** and
   "No taps yet" with the state reset.

### C4 - New code with a side effect (print) via Hot Reload

1. I temporarily added `print('oi')` at the start of `_incrementCounter()` (the
   Increment FAB callback) in `lib/main.dart`.
2. Hot reload (`fullRestart: false`), `Reloaded application in 471ms.`
   (`code: 0`).
3. I clicked the Increment FAB: the `flutter run` tool window/console showed the
   line **`oi`** on stdout. Hot reload loaded the new version of the method
   (with the print) and it started running on click, without restarting the app.
4. I removed the `print('oi')` at the end.

### C5 - Adding a dependency while the app runs

1. With `flutter run` still active, I ran `flutter pub add intl` in the project
   directory. Output: `+ intl 0.20.3` / `Changed 1 dependency!`.
2. `pubspec.yaml` then contained `intl: ^0.20.3` (in `dependencies`).
3. I applied hot reload (480 ms, `code: 0`) and the app kept working normally:
   the dump showed counter **3** and the message "A few taps" (the C4 click
   state remained), confirming the app kept running with the new dependency
   resolved.
4. Keeping the `intl` dependency (intended permanent change of the exercise).

### C6 - Summary of what was observed

- **Hot reload (`r`)** applies code changes (texts, themes, methods) in about
  ~0.4-0.6 s and **preserves the screen state** (the counter stayed the same),
  including not re-running field initializers.
- **Hot restart (`Shift+R`)** re-runs `main()`: it recreates the app, **resets/
  loses state** and applies the initial code values; on Edge it took ~0.5-1.5 s
  and spawned a new isolate.
- Both happen **without closing the app window**; texts and colors change on the
  screen in real time, and new prints appear in the tool console after the
  reload.
- Adding/changing dependencies (`flutter pub add`) with the app open is picked
  up by hot reload without needing a full restart.
- The Web app experiment kept the expected fast-development behavior typical of
  Android/iOS emulators.

## Part D - Environment logbook

### D1 - Problems found

Sources consulted (real records):

* terminal history (PowerShell `ConsoleHost_history.txt`);
* current output of `flutter doctor -v` and `flutter devices`;
* log files of the run session (`run_stdout.log` of `flutter run --machine`);
* the VMService dumps used in Part C (`dump_stale_isolate.json`, etc.).

> Note: where no time record existed, the field reports that limitation instead
> of estimating a value that was not measured at the time.

### Problem 1

**Operating system:** Microsoft Windows 11 Home (25H2, build 10.0.26200.9457) - 64-bit

**When:** environment check (`flutter doctor -v`)

**Error message (copied, not typed):**

```text
[X] Chrome - develop for the web (Cannot find Chrome executable at .\Google\Chrome\Application\chrome.exe)
    ! Cannot find Chrome. Try setting CHROME_EXECUTABLE to a Chrome executable.
```

**What I tried that DID NOT work:**

* the `CHROME_EXECUTABLE` variable **is not set** in any scope (User, Machine
  or Process) - checked with
  `[Environment]::GetEnvironmentVariable('CHROME_EXECUTABLE', ...)`.
* the terminal history records an attempt to run `flutter run -d chrome`
  (line 270), which could not open any window since Chrome is not installed.

**What solved it:**

* using **Edge** as the web browser (`flutter run -d edge`), which appears in
  `flutter devices`; `flutter doctor` still reports the missing Chrome.

**Time spent:** not timed then (doctor ran together with the other checks).

**How I found out:** output of `flutter doctor -v` run during the Part D analysis.

### Problem 2

**Operating system:** Microsoft Windows 11 Home (25H2, build 10.0.26200.9457) 64-bit

**When:** environment check (`flutter doctor -v`, current state)

**Error message (copied, not typed):**

```text
X Android license status unknown.
  Run `flutter doctor --android-licenses` to accept the SDK licenses.
  See https://flutter.dev/to/windows-android-setup for more details.
```

**What I tried that DID NOT work:**

* the terminal history records that `flutter doctor --android-licenses` was
  already run, but the current `flutter doctor` still marks "Android license
  status unknown." even though the license files **exist** and have the correct
  hashes in `...\Android\sdk\licenses\android-sdk-license` and
  `android-sdk-preview-license`).

**What solved it:**

* **nothing yet, as of today.** When running `flutter doctor --android-licenses`,
  the tool replied that the option is no longer needed, because the new Android
  CLI replaced `sdkmanager`:

  ```text
  WARNING: The SDK Manager CLI tool (sdkmanager) is deprecated. Android CLI will be used instead.
  Warning: The --licenses option is no longer needed.
  ```

  In other words: the licenses are accepted in the files, but flutter doctor
  3.47.1 still cannot verify them with the new Android SDK 37.0.0, so the item
  stays `[!]`.

**Time spent:** not timed then.

**How I found out:** current output of `flutter doctor -v` + command recorded in
the terminal history.

### Problem 3

**Operating system:** Microsoft Windows 11 Home (25H2, build 10.0.26200.9457) 64-bit

**When:** Android SDK installation/configuration (NDK installation)

**Error message (copied, not typed):**

```text
[the exact error text is not in the available records; only the commands were saved]
```

**What I tried that DID NOT work** (real attempts from the terminal history):

* `sdkmanager --install "ndk;28.2.13676358"`
* `cd C:\Users\nb\AppData\Local\Android\sdk\cmdline-tools\latest\bin` followed by
  `.\sdkmanager.bat "ndk;28.2.13676358"`
* `android sdk install ndk`
* `C:\Users\nb\AppData\Local\Android\sdk\cmdline-tools\latest\bin\android.bat sdk list ndk`

**What solved it:**

* in the end the NDK was installed: the folder
  `C:\Users\nb\AppData\Local\Android\sdk\ndk` now contains `28.2.13676358` and
  `30.0.15729638`, but the records do not allow identifying which attempt
  completed it.

**Time spent:** not timed then.

**How I found out:** real chronological sequence from the terminal history
`sdkmanager --install "ndk;28.2.13676358"` (no path), then
`cd ...cmdline-tools\latest\bin` + `.\sdkmanager.bat "ndk;28.2.13676358"`, then
`android sdk install ndk` and `android.bat sdk list ndk`, interleaved with
`flutter doctor --android-licenses` and `dir` checks in **two different SDK
paths** (`C:\nb.code\Android` and `C:\Users\nb\AppData\Local\Android\sdk`) plus
the current state of the `...\sdk\ndk` folder (contains `28.2.13676358`,
exactly the target version of the attempts, and `30.0.15729638`).

### Problem 4

**Operating system:** Microsoft Windows 11 Home (25H2, build 10.0.26200.9457) 64-bit

**When:** device connection during execution (Part C experiments)

**Error message (copied, not typed):** there was no error message; the Android
device simply was not available. Real `flutter devices` output at the time:

```text
Found 2 connected devices:
  Windows (desktop) • windows • windows-x64    • Microsoft Windows [Version 10.0.26200.9457]
  Edge (web)        • edge    • web-javascript • Microsoft Edge 153.0.4234.32
```

**What I tried that DID NOT work:**

* the history shows a **physical phone** was used in a previous session
  (`flutter run -d R9XN70CESWD`); at the time of Part C it was not connected
  and there was no emulator listed.

**What solved it:**

* running the app on the **web (Edge)**: `flutter run -d edge`.
* **no emulator was created**: the Emulator package `37.1.11.0` is installed in
  the SDK, but `flutter emulators` answers **"No emulators available."**
  (no AVD created).

**Time spent:** not timed then.

**How I found out:** `flutter devices` output + terminal history
(`flutter run -d R9XN70CESWD`, `flutter run -d chrome`).

### Problem 5

**Operating system:** Microsoft Windows 11 Home (25H2, build 10.0.26200.9457) - 64-bit

**When:** running the app and hot restart (`fullRestart: true`) on Edge (Part C - C3)

**Error message (copied, not typed), occurred 2 times during the restarts:**

```text
"Trying to render a disposed EngineFlutterView."
Assertion failed: org-dartlang-sdk:///lib/_engine/engine/window.dart:99:12
The following assertion was thrown during a scheduler callback:
!isDisposed
```

**What I tried that DID NOT work:**

* nothing; the exception was transient and did not stop the restart.

**What solved it:**

* the hot restart itself continued and finished normally
  (`Restarted application in 1,515ms.` / `479ms.`, `result.code: 0`), and the
  app kept working.

**Time spent:** 1,515 ms and 479 ms (real times from the log)

**How I found out:** session log file `run_stdout.log` of
`flutter run --machine` (the C3 restart lines).

### Problem 6

**Operating system:** Microsoft Windows 11 Home (25H2, build 10.0.26200.9457) - 64-bit

**When:** running the app and automating `flutter run --machine` (Part C)

**Error message (copied, not typed):**

```text
[there is no error message; the daemon simply did not answer the commands;
no response line was emitted on stdout]
```

**What I tried that DID NOT work:**

* sending JSON-RPC commands in the format `{"method":"app.restart","params":{...}}`
  (without the square brackets); the daemon silently ignored them, including
  invalid commands.

**What solved it:**

* following the real protocol format: every input message must be a line starting
  with `[{` and ending with `}]`, with **a single object inside the brackets**
  (class `DaemonInputStreamConverter` in
  `packages\flutter_tools\lib\src\daemon.dart`). After that, responses started
  appearing in the log, e.g.:
  `[{"id":7,"result":{"code":0,"message":""}}]`

**Time spent:** not timed then.

**How I found out:** comparing the sent commands (`sent.txt`) with the absence of
response in `run_stdout.log`, together with reading the Flutter SDK source code.

### Problem 7

**Operating system:** Microsoft Windows 11 Home (25H2, build 10.0.26200.9457) - 64-bit

**When:** running the app and collecting state via the Dart VM Service after a
hot restart (Part C)

**Error message (copied, not typed), real VM service response:**

```text
{"jsonrpc":"2.0","result":{"type":"Sentinel","kind":"Collected","valueAsString":"Unrecognized isolateId: 1"},"id":90758}
```

**What I tried that DID NOT work:**

* using the old isolate id (`1`) to call `ext.flutter.debugDumpApp` after the
  hot restart; the restart recreates the isolate with another id.

**What solved it:**

* re-reading the isolate list with `getVM` and using the current id (in the
  session: `775` and, after another restart, `1549`).

**Time spent:** not timed then.

**How I found out:** real VM service response saved in `dump_stale_isolate.json`.

### Machine configuration

- **Operating system:** Microsoft Windows 11 Home (25H2) detected automatically
- **Version:** 10.0.26200.9457 (64-bit) detected automatically
- **RAM:** 7.3 GB total (0.2 GB free at check time), detected automatically
- **Device used:** physical phone (Android, serial `R9XN70CESWD`) in a previous
  session (`flutter run -d R9XN70CESWD`); in Part C **Edge (web)** was used
  with no emulator configured.

Environment resources detected automatically:

- Flutter `3.47.1` (stable), Dart `3.13.1`
- Android SDK `37.0.0` at `C:\Users\nb\AppData\Local\Android\sdk`
  (NDK `28.2.13676358` and `30.0.15729638`; Emulator `37.1.11.0`)
- Java: OpenJDK `25.0.2` (bundled with Android Studio at
  `C:\nb.code\Android Studios\jbr`)
- Visual Studio Community 2026 `18.9.1` (Windows 10 SDK `10.0.26100.0`)
- Browser: Microsoft Edge `153.0.4234.32`

### D2 - Reflection

**(a) Which was the most confusing step of the installation, and what would have made it clearer?**

The most confusing step, according to the terminal history, was the **NDK
installation of the Android SDK through the command line**: several different
attempts were recorded in sequence (`sdkmanager --install "ndk;28.2.13676358"`
without a path; then `sdkmanager.bat` from `cmdline-tools\latest\bin`; then
`android sdk install ndk`; then `android.bat sdk list ndk`), interleaved with
`dir` checks in **two different SDK paths** (`C:\nb.code\Android` and
`C:\Users\nb\AppData\Local\Android\sdk`) - a real sign of uncertainty about
which executable to use and from which folder to run it. Documentation pointing
to the exact manager path
(`C:\Users\nb\AppData\Local\Android\sdk\cmdline-tools\latest\bin\sdkmanager.bat`)
and printing the tool's error messages (which today are not preserved in any
record) would have made it clearer.

**(b) Did you use a physical phone or an emulator? Why? If you used an emulator, how long did it take to open?**

According to the terminal history, a **physical phone** was used (Android, serial
`R9XN70CESWD`) with `flutter run -d R9XN70CESWD`. An emulator was **not** used:
it did not appear in the device list (`flutter devices`), so connecting the
phone and, later, running on the **web (Edge)** were the real paths. Since I did
not use an emulator, there is no opening time to report.

**(c) How long did the first `flutter run` take, and how long did the second one?**

The original history **did not record** the duration of the `flutter run` calls
made in class. To avoid leaving it blank, I measured again, on the same project
and environment, **two consecutive `flutter run -d edge` runs on 19/09/2026**
(timing from launch until the `Flutter run key commands` / `R Hot restart`
line):

```text
First flutter run: 35.3 s
Second flutter run:  31.3 s
```

The second one was slightly faster because it reuses what is already cached, the
same pattern described in the material ("the first time takes long; the next
ones take seconds"), except that here, being web (Edge), there is no Gradle
download as there is on Android.