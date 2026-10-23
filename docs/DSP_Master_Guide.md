# DSP Master Guide — HMMY458 Digital Signal Processing

**Greek title:** Ψηφιακή Επεξεργασία Σήματος · **Academic year:** 2026–2027.
**Course identity:** eClass uses **HMMY458**; the page and Lab 1 PDF also identify the course as **ΤΗΛ301**.
**Verified:** 16 October 2026, against the current Lab 1 PDF, eClass assignment and laboratory announcement. Times below are local Greece time (Europe/Athens).

**Shared repository:** [DSP projects](https://github.com/peterkontellis-spec/PSIFIAKI-EPEKSERGASIA-SYSTHMATOS). The repository copy at `docs/DSP_Master_Guide.md` is the maintained shared guide; `STATUS.md` at the repository root tracks joint progress. Read both before repository changes and update status after each change batch.

**Working reference:** This is the maintained master guide for the DSP chat, as requested by the user on 16 October 2026. Use it as the main reference unless the user directs otherwise. Update verified course requirements from official HMMY458 sources and record actual work progress separately from assumptions. Keep DSP and ΨΥΣ course information separate.

**Latest update — 23 October 2026:** fixed stale generated figures and completed the required 3A magnitude plot using the explicit radians convention. At 128 samples and 256 Hz, radians/degrees give the same magnitudes within `1e-12`; the phase unit remains unconfirmed but does not block this result. All 18 numerical/rerun tests passed and all eight default figures reproduced byte-for-byte. See [shared status](../STATUS.md) and [verification evidence](../lab1/VERIFICATION.md). Owners and group naming remain open. The final 1B Hz plot still awaits its physical sampling rate. No final ZIP or submission has been made. Live eClass dates were last checked on 16 October; the supplied assignment gives 29 October at 23:30.

**Independent review — 23 October 2026:** a Python expert reviewed implementation commit `1d70f60`. All 15 tests and seven clean-copy figure reproductions passed; no numerical defect was found. A stale-output issue was reproduced when default runs follow explicit-parameter runs. Final figures and ZIP remain unfinished. See the scorecard and findings in [STATUS.md](../STATUS.md). No solution code was changed during this review. The subsequent fix and completed 3A plot are recorded above; the original scorecard remains tied to the reviewed commit.

**Independent re-review — 23 October 2026:** the expert reviewed `1c7c2df`, independently passed all 18 tests and reproduced all eight figures exactly. Stale outputs are fixed and 3A is complete. Scores for compliance, mathematics, clarity, testing and readiness are **9 / 9 / 9 / 9 / 7.5**. Remaining: 1B’s physical scale and plot; final instructions containing the agreed `--fs` value; a short report theory completion using the existing assignment formulas; team identification; and the actual extracted-ZIP check and upload. See the detailed checklist in [STATUS.md](../STATUS.md). The theory additions are a reviewer interpretation of the report requirements, not extra numerical methods. No live deadline recheck was performed.

**Report theory completed — 23 October 2026:** added the DFT/inverse pair from assignment p. 1, the ideal low-pass reconstruction model from p. 2, and FFT bin spacing/axis conventions from preparation pp. 18/22. All 18 tests passed again; direct checks of the written transform formulas and bin mapping passed within `1e-10`. A local report preview includes the eight existing figures. 1B’s sampling rate and group details remain open by instruction. No solution code changed and no eClass submissions were accessed or changed.

## 1. Immediate priorities and deadlines

| Action | Deadline / timing | Verified source |
|---|---|---|
| First-time laboratory students: register electronically in a user group if not already registered | **Sunday 18 October 2026, 23:30** | [Laboratory announcement][D3] |
| Lab 1 implementation tutorial and questions | **Thursday 22 October 2026, 11:00–12:00** | [October 15 announcement][D8]; course teaching room, no room number specified |
| Submit Lab 1 | **Thursday 29 October 2026, 23:30** | [Assignment][D1] and [PDF, p. 4][D2] |
| Mandatory written laboratory examination | On the course examination day during the examination period; initially January, with September provided for those unable to participate in the first period | [Laboratory announcement][D3]; exact calendar date/time not established |

**Lab 1 upload:** one **ZIP** containing **Python code and a detailed report**, with short execution instructions accompanying the separate code files. The assignment is marked as a group assignment and graded out of 10. [Source][D1]

**Current registration status:** The signed-in eClass account is shown as belonging to **Ομάδα Χρηστών 69**, marked **Η Ομάδα Μου**, with **3/3 members**. Registration is therefore shown as complete for this account as of 16 October. The October 18 deadline remains the official deadline for students not yet registered. [Group page][D5]

**Correction to earlier chat context:** The earlier DSP chats associated the work with Group 41 and a GitHub repository described as Group 41. The live eClass membership now shows Group 69; this is historical membership evidence; **final project/group naming remains open by user instruction on 22 October**. The repository's current group label and its relationship to Group 69 have not been checked. Do not infer eClass registration from a repository name or description.

## 2. Group, attendance and grading rules

The October 13 [laboratory announcement][D3] states:

- First-time laboratory students complete **four exercises** during the semester and submit them electronically through eClass **Εργασίες**.
- Exercises are implemented/submitted in groups of **at most three students**, according to electronic group registration.
- Students who have not registered in a user group must do so by **October 18 at 23:30**, in the first-time laboratory participation context.
- Roughly **two weeks** are allowed from release to delivery. Use each assignment’s actual deadline, not this approximate interval.
- **Physical attendance in the laboratory to carry out exercises is not compulsory.**
- Optional in-person help is offered **Mondays 14:00–15:00**, office **141.Α33**, at the end of the first-floor corridor. Available computers or personal laptops can be used.
- Questions can also be addressed in class or by email.
- An intermediate tutorial is announced separately, usually **Thursday 11:00–12:00**, in the course’s scheduled teaching room. This is a usual window, not a verified date for every tutorial.
- The laboratory contributes **15%** of the final course grade, calculated as the mean of the **four equally weighted exercise grades**, subject to the written-exam condition below.

The announcement also addresses students eligible to retain laboratory credit from **2023–24, 2024–25 and 2025–26**. It does not, by itself, verify any particular student’s eligibility. The mandatory written examination applies to them too.

## 3. Exactly what to implement in Python

Lab 1 contains **three exercises**, with subparts. The PDF’s first two pages give theoretical background on DFT/inverse DFT, convolution, sampling, aliasing and ideal reconstruction; the implementation questions are on pages 3–4. [PDF][D2]

### Exercise 1 — Discrete sequences, convolution and FFT

#### A. Create the sequences and implement convolution

Use the exact sequences:

```text
x[n] = 10 - n       for -4 ≤ n ≤ 4; 0 elsewhere
y[n] = 0.8^(n+1)    for -2 ≤ n ≤ 5; 0 elsewhere
```

- [ ] Create and plot both discrete-time sequences.
- [ ] Calculate their convolution **from the convolution formula**, rather than using only a library convolution call.
- [ ] Display both initial sequences and the convolution result.
- [ ] Verify against **`numpy.convolve` or `scipy.signal.convolve`**.
- [ ] Explain how each input sequence’s length affects the output.

**Derived checks:** the nonzero sequences have lengths **9** and **8**. Full linear convolution has **16** samples, with index support **−6 through 9**. Keep physical sequence indices distinct from zero-based array positions. These values are mathematical checks derived from the supplied sequences. [PDF, p. 3, Exercise 1A][D2]

#### B. Frequency-domain representation

- [ ] Use **`numpy.fft.fft`** to transform the signals.
- [ ] Plot their **magnitude spectra on the same graph**, with frequency in **Hz**.
- [ ] Make the sample interval/frequency assumption explicit; see the uncertainty below.

The wording refers to the preceding signals. At minimum show the two input spectra together; including a clearly labelled convolution spectrum as well is a prudent way to cover the broader interpretation, not an explicitly enumerated third spectrum requirement. [PDF, p. 3, Exercise 1B][D2]

#### C. Demonstrate the convolution theorem

- [ ] Show that convolution in time corresponds to multiplication in frequency for the supplied sequences.
- [ ] Explain the relation and demonstrate agreement numerically/graphically.

**Implementation guidance, not an extra official constraint:** use a common FFT length of at least **16** for linear-convolution comparison. Insufficient padding makes the inverse FFT of the product a circular convolution. Align sequence origins consistently when comparing transforms. State any numerical tolerance used.

**Unspecified parameter:** the PDF supplies discrete indices but no sampling rate for Exercise 1, while requesting a Hz axis. State and justify an assumed sample interval, such as 1 second if using that convention, or ask staff which scale they intend. Do not present an assumed value as prescribed.

Suggested libraries/functions in the brief include NumPy, Matplotlib, optionally SciPy Signal, `numpy.linspace`, `plt.plot`, `plt.stem`, `numpy.fft.fft`, and `numpy.fft.fftfreq`. [PDF, p. 3][D2]

### Exercise 2 — Sampling and reconstruction

The exact signal and initial interval are:

```text
x(t) = 20 cos(10πt) - 40 sin(5πt)
0 < t < 500 ms   (= 0.5 s)
```

#### A. Continuous-time signal representation

- [ ] Create and plot the signal in Python on the specified interval.
- [ ] Use a sufficiently fine numerical time grid to represent the continuous curve, and document that choice.

#### B. Spectrum and Nyquist rate

- [ ] Transform the signal into the frequency domain, `X[f]`.
- [ ] Find and state the signal’s Nyquist sampling rate in the report.

**Derived theory checks:** `10π = 2π·5`, so the cosine is **5 Hz**; `5π = 2π·2.5`, so the sine is **2.5 Hz**. The highest frequency is **5 Hz**, giving a Nyquist rate of **10 samples/s**. Distinguish this signal-dependent rate from the Nyquist frequency `fs/2` of a chosen sampling system.

#### C. Three sampling periods and interpretation

| Required period | Corresponding sampling rate |
|---|---|
| `Ts = 1/20 s` | `fs = 20 Hz` |
| `Ts = 1/10 s` | `fs = 10 Hz` |
| `Ts = 1/5 s` | `fs = 5 Hz` |

- [ ] For **each** period, plot the original signal and its sampled representation together.
- [ ] Explain what happens to the reconstructed signal as the sampling period changes, and why.
- [ ] Address whether the reconstructed result changes when the original plotting interval becomes **`0 < t < 5000 ms`**, i.e. **5 seconds**.

**Implementation as of 22 October:** follows the preparation notes’ original-curve and sampled-point plots, with a written discussion of reconstruction from the specified theory. No numerical interpolation or reconstruction routine is added. A longer observation interval changes spectral resolution and finite-record effects; it does not raise the sampling rate or remove aliasing by itself.

Treat **10 Hz** as the boundary case, not a blanket guarantee for all signal phases at the Nyquist limit. For this exact signal the highest-frequency term is a cosine; discuss the actual samples and phase rather than claiming every sinusoid at the boundary vanishes. [PDF, pp. 2–3][D2]

### Exercise 3 — Sampling choices and aliasing

#### A. 128 samples without aliasing

The PDF writes:

```text
x(t) = 12 cos(2π·20t) - 18 sin(2π·60t + 30)
```

- [x] Choose a sampling frequency that avoids aliasing.
- [x] Generate **128 samples**.
- [x] Plot the spectrum with the horizontal axis in **Hz**.
- [x] Explain the sampling-rate selection criterion.
- [x] Discuss a wider range of acceptable sampling frequencies.

**Derived guidance:** the highest sinusoidal frequency is **60 Hz**. Choosing **`fs > 120 Hz`** avoids relying on an exact Nyquist-boundary case. A convenient example is **256 Hz**, giving a 2 Hz FFT-bin spacing for 128 samples; this is a suggested choice, not an assigned value.

**Phase ambiguity:** the printed expression is `+30`, with no degree symbol or explicit unit. Standard mathematical/Python trigonometric convention would interpret this as radians, but **30 degrees has not been verified as the intended meaning**. State your interpretation or ask staff; do not silently convert it.

**Completed — 23 October:** the [3A plot](../lab1/figures/ex3a_spectrum.png) uses 256 Hz and 128 samples with `+30` explicitly treated as radians. The 20/60 Hz tones occupy distinct FFT bins 10/30, so their normalized magnitudes are 6/9 regardless of the sine phase. Comparing radians and degrees across all bins gave a maximum difference of `3.762e-14` (tolerance `1e-12`). The waveform samples differ; this invariance claim is specific to the chosen record and frequencies. See the [report](../lab1/report.md).

#### B. Fixed sampling rate of 20 kHz

Start with:

```text
x(t) = sin(2π f0 t + φ)
fs = 20,000 Hz
```

- [ ] Write the discrete-time expression and explain its derivation:

```text
x[n] = sin(2π (f0 / 20000) n + φ)
```

- [ ] Generate signals at **500, 1000, 1500 and 2000 Hz**.
- [ ] Plot the spectrum of **each** and explain the observed behavior.
- [ ] Repeat for **18000, 18500, 19000 and 19500 Hz**.
- [ ] Explain the aliasing in the second set.

**Derived study checks:** at a 20 kHz sample rate, the second set has baseband alias magnitudes **2000, 1500, 1000 and 500 Hz**, respectively. For a sine, account for sign/phase: matching magnitude-spectrum peaks does not necessarily imply identical sample values with the same phase. State whether your plot uses a one-sided or two-sided frequency axis.

The brief does **not** assign a numerical `φ` or a sample count for **3B**. Specify your choices and use them consistently; the **128-sample** requirement is explicitly stated in **3A**, not independently in 3B. [PDF, p. 4][D2]

## 4. Exact upload and report requirements

Submit **one ZIP** via the [Lab 1 eClass assignment][D1], by **29 October 2026 at 23:30**. The upload form allows one file and displays a maximum size of **1024M**.

The ZIP must contain:

1. **Python code**, with comments explaining key parameters and variables.
2. A **detailed report** on the results.
3. **Short execution instructions** accompanying the separate code files.

The report must:

- Include the theoretical knowledge and formulas needed to implement the questions and verify the results.
- Include the graphs/figures produced for **every question**.
- Keep the Python code **separate from the report**, rather than inserting the code listings as the report content.
- Give each graph a **main title and labelled axes**, showing the useful signal range needed to draw conclusions.
- Briefly explain the implementation for each question, how quantities were calculated, and which theoretical relationship guided the work.
- Include observations and conclusions, demonstrating reasoning rather than simply presenting program output.

These requirements appear both in the assignment description and the PDF. [Assignment][D1], [PDF, p. 4][D2]

### Suggested package layout — not a required naming convention

```text
DSP_Lab1_GroupXX.zip
  report.pdf
  README.txt
  exercise1.py
  exercise2.py
  exercise3.py
```

PDF is a practical report format, but the reviewed sources do not explicitly mandate the report extension. Script organization and ZIP filename above are suggestions. A requirements file and saved figures may help reproducibility but are not separately listed as compulsory deliverables. Do not assume a notebook alone replaces the requested separate code and detailed report.

## 5. Mandatory examination: official requirements

The [October 13 announcement][D3] verifies:

- **All students** must take the written laboratory examination, including first-time students and students eligible to retain laboratory grades from 2023–24, 2024–25 or 2025–26.
- It is a **30-minute written examination** with **multiple-choice questions**.
- It takes place on the **course examination day during the examination period**.
- The laboratory questions are distributed together with the theoretical-course examination questions.
- January is the initial examination period; September is mentioned for those unable to take part in the first period.
- The laboratory grade can count/be retained **only if the written laboratory examination grade is at least 5**.

**Important distinction:** optional physical attendance while developing the exercises does not make this written examination optional.

### Not officially established in the reviewed sources

The exact exam date/time, number of questions, negative marking, allowed notes/calculator, detailed topic weighting and exact question list are not specified. The announcement does not restrict the exam to Lab 1. A Lab 1 guide is therefore **not a complete semester exam syllabus**. It also does not fully describe every consequence or resit procedure for a failed or missed written lab exam.

## 6. Exam preparation based on Lab 1 — study advice

These topics are inferred from the lab’s theory and implementation, not a verified official question list:

- DFT versus FFT; inverse DFT; meaning of a complex spectrum and its magnitude/phase.
- Constructing a frequency axis in Hz from `fs`, `N` and `fftfreq`; bin spacing `Δf = fs/N`.
- Linear convolution, index support, and the length formula `Nx + Ny - 1`.
- The convolution theorem, circular versus linear convolution and zero-padding.
- Sampling period versus sampling frequency: `Ts = 1/fs`.
- Converting `cos(Ωt)` or `sin(Ωt + φ)` into frequency in Hz, and then a discrete-time expression.
- The Nyquist sampling criterion and the special behavior of boundary cases.
- Why frequencies separated by multiples of `fs` can produce aliases, including sign/phase for sine waves.
- Ideal low-pass/sinc reconstruction and the limitations of finite sampled records.
- How a longer record changes FFT resolution, and why it does not undo aliasing.
- Your own code, parameter choices, plots and theoretical explanations for every subquestion.

**Recommended self-check:** explain the 16-sample convolution length, the 5 Hz/2.5 Hz components in Exercise 2, the >120 Hz sampling choice in 3A, and all four aliases in 3B without referring to code.

## 7. Final checklists

### Registration

- [x] Electronic registration verified for the signed-in eClass account: **Group 69**, checked 16 October 2026.
- [x] Current group contains **3/3 members**, within the maximum of three.
- [x] Registration is shown as complete before **18 October 2026, 23:30** for this account.
- [ ] If relying on retained credit, verify personal eligibility separately.

### Implementation and report

- [ ] Exercise 1: both sequences, formula-based convolution, library verification, correct indices/length, spectra and convolution theorem.
- [ ] Exercise 2: specified signal, initial 0.5-second interval, spectrum/Nyquist reasoning, all three sampling periods and 5-second comparison.
- [x] Exercise 3A: 128 samples, justified alias-free sampling rate, Hz spectrum, phase interpretation recorded; verified 23 October.
- [ ] Exercise 3B: discrete-time formula, all eight specified frequencies, spectra and alias explanations.
- [ ] Assumptions about sample intervals, phase, reconstruction and record lengths are explicit.
- [ ] Every graph has a title, labelled axes and useful limits.
- [ ] Every subquestion has theoretical reasoning and conclusions in the report.
- [ ] Python files contain meaningful comments and are separate from the report.
- [ ] Execution instructions describe dependencies and how to run the code.

### Submission and examination

- [ ] ZIP opens correctly and contains the report, code and execution instructions.
- [ ] Code runs after extracting into a fresh folder, with all necessary files included.
- [ ] Submit one group ZIP **before 29 October 2026, 23:30**.
- [ ] Verify the submission in eClass and retain the uploaded copy/confirmation.
- [ ] Each member studies the lab concepts and follows later exam announcements.
- [ ] Plan to attend the mandatory 30-minute exam and meet the **≥5** condition.

## 8. Uncertainties and assumptions register

| Item | What is known / what remains open |
|---|---|
| Exercise 1 frequency units | Hz is requested; no physical sample interval is supplied. Declare an assumption or obtain clarification. |
| Exercise 1B spectra | The wording refers to the preceding signals without an explicit list; show both inputs together and consider including the convolution spectrum clearly labelled. |
| Exercise 2 reconstruction | Uses original/samples plots from the preparation and written theory; no additional reconstruction algorithm. |
| Exercise 3A phase | `+30` is printed without units. Radians are explicitly used; the requested magnitude is complete because the two interpretations agree within tolerance at the chosen bins. Instructor intent remains unconfirmed. |
| Exercise 3B phase and record length | Neither a numerical phase nor a sample count is prescribed for this subpart. |
| Report/ZIP naming | ZIP is compulsory; report extension and filename conventions are not established. |
| Late submission policy | The deadline is verified; a specific late penalty or extension rule was not verified. |
| Exam details | Format, duration, scope of participation and ≥5 condition are confirmed; exact questions/date/materials are not. |
| Credit retention | Eligible prior academic years are listed; individual eligibility is not verified here. |

The supplied guide was originally reconstructed from official course sources when the chat reader returned placeholders. The DSP chat subsequently recovered the earlier answers through the browser. The official-source detail in this guide remains the main reference; earlier chat summaries do not override it. Recheck announcements when updating this guide after 16 October 2026.

## 9. Current work status and update record

| Item | Status / evidence date | Evidence / next action |
|---|---|---|
| Group registration | **Complete for the signed-in account: Group 69, 3/3 members** | Live [group page][D5] marks it as `Η Ομάδα Μου`. |
| Assignment availability | **Only Lab 1 currently listed** | Live [assignment list][D9] contains one assignment; no Lab 2–4 briefs or deadlines established in this check. |
| Lab 1 deadline | **29 October 2026, 23:30**, unchanged | [Assignment][D1] and [October 15 announcement][D8]. |
| Lab 1 implementation/report | **In progress, 23 October** | Three scripts, eight figures and 18 passing checks. Stale outputs fixed; 3A magnitude and report theory additions complete. Final 1B plot and package remain pending; see [STATUS.md](../STATUS.md). |
| Lab 1 submission | **No submission shown for the signed-in account** | Assignment list has no entry under `Έχει υποβληθεί`; assignment detail presents an upload form without a submission record. This does not independently establish whether a teammate has submitted elsewhere. |
| Tutorial | **22 October 2026, 11:00–12:00** | [October 15 announcement][D8]; includes time for questions about implementation. |
| Course calendar | **No dated events visible in the October month view during this check** | [Calendar][D7]. Use the explicit announcements and assignment deadline; do not infer dates from an empty calendar. |
| Written lab exam | **30 minutes, multiple choice, grade ≥5 required for lab credit** | [Laboratory announcement][D3], verified earlier in this DSP chat on 16 October; exact date/time and permitted materials remain open. |
| Earlier Group 41 repository reference | **Needs reconciliation with current Group 69 membership** | User confirmed [this DSP repository][D10]. Its initial README does not state a group number; earlier Group 41 references do not override current eClass membership. |

### Provisional dates found in the repository README

The repository's `README.txt`, inspected on 16 October 2026 at initial commit `d2346ae`, lists these dates. They have **not been verified against official eClass announcements or assignment pages**, and no cutoff times are given. They do not mean the later assignments are already published.

| Lab | Listed release | Listed deadline | Status |
|---|---|---|---|
| 2 | 30 October 2026 | 13 November 2026 | Provisional; README only |
| 3 | 13 November 2026 | 27 November 2026 | Provisional; README only |
| 4 | 3 December 2026 | 20 December 2026 | Provisional; README only |

### Update log

- **23 October 2026 — report theory:** completed the requested formulas strictly from the supplied sources and created a local preview. All 18 tests and direct formula/bin checks passed; 1B and group decisions remain open. eClass submissions untouched.

- **23 October 2026 — re-review:** recorded the updated expert scores and exact remaining submission checklist. Independent checks confirm 18 tests, eight exact figure reproductions and both resolved findings; no solution code changed.

- **23 October 2026 — fixes:** resolved stale generated figures and completed the 3A magnitude plot and explanation. Verified phase independence within `1e-12`, 18 passing tests and eight byte-for-byte figure reproductions. 1B and the final package remain pending.

- **23 October 2026:** Recorded the independent expert review in shared status: numerical checks passed; stale-output behavior needs attention; final figures and ZIP remain pending.

- **22 October 2026:** Applied the supplied preparation notes; added the first verified Lab 1 implementation, seven figures and working report. Kept owners, group naming and unclear parameters open. Verification details are recorded in `lab1/VERIFICATION.md`.

- **16 October 2026:** User confirmed the shared DSP repository. Inspected the initial README-only state; added repository `STATUS.md`, agent maintenance instructions and this shared guide. Recorded Labs 2–4 README dates as provisional.

- **16 October 2026:** Adopted the user's supplied master guide as this chat's main DSP reference and saved this maintained copy in the chat's outputs.
- **16 October 2026:** Rechecked all four currently listed announcements at the listing level and read the October 15 Lab 1/tutorial announcement. No newer announcement or deadline change was visible.
- **16 October 2026:** Added the confirmed October 22 tutorial, verified Group 69 membership, and separated registration, implementation and submission status.
- Future updates should record the verification date, source, changed deadline/requirement or evidenced work completed. Do not mark code, report or submission complete merely because it has been planned.

## Sources

All sources below belong to **HMMY458**. eClass may require sign-in.

- [D1 — Lab 1 assignment: deadline, ZIP contents, report requirements and upload form][D1]
- [D2 — Lab1_2026.pdf: theory pp. 1–2; Exercises 1–2 p. 3; Exercise 3 and deliverables p. 4][D2]
- [D3 — October 13 laboratory announcement: groups, registration, attendance, grading and mandatory written exam][D3]
- [D8 — October 15 Lab 1 announcement: submission deadline and October 22 tutorial][D8]
- [D9 — Current assignment list and submission status][D9]
- [Course home][D4] · [Group registration / membership][D5] · [Announcements][D6] · [Calendar][D7]

[D1]: https://www.eclass.tuc.gr/modules/work/index.php?course=HMMY458&id=18842
[D2]: https://www.eclass.tuc.gr/modules/work/index.php?course=HMMY458&get=18842&file_type=1
[D3]: https://www.eclass.tuc.gr/modules/announcements/index.php?course=HMMY458&an_id=71611
[D4]: https://www.eclass.tuc.gr/courses/HMMY458/
[D5]: https://www.eclass.tuc.gr/modules/group/index.php?course=HMMY458
[D6]: https://www.eclass.tuc.gr/modules/announcements/index.php?course=HMMY458
[D7]: https://www.eclass.tuc.gr/modules/agenda/index.php?course=HMMY458

[D8]: https://www.eclass.tuc.gr/modules/announcements/index.php?course=HMMY458&an_id=71674
[D9]: https://www.eclass.tuc.gr/modules/work/index.php?course=HMMY458
[D10]: https://github.com/peterkontellis-spec/PSIFIAKI-EPEKSERGASIA-SYSTHMATOS

## Supplied preparation notes

`Lab1-Preparation.pdf` (30 pages), supplied on 22 October 2026: convolution/index support pp. 4–9, sampling/Nyquist pp. 18–21, FFT conventions and examples pp. 22–25. It supplies teaching methods, not additional assignment tasks. Exact source-copy fingerprints and the question-to-method mapping are in [VERIFICATION.md](../lab1/VERIFICATION.md).
