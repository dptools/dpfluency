# Clarity Quantifier

This is a simple tool, that uses verbaitim transcripts (from [TranscribeMe!](https://www.transcribeme.com/)), to compute the following metrics:

| Language Features         | Definition                                                                                                 | Measured Skill                                          |
|---------------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Words per turn            | Mean number of words per turn                                                                              | Sentence complexity, Verbosity                          |
| Words per second          | Total words produced by the subject over total duration of subject's turn                                  | Speed of speech production                              |
| Disfluencies per turn     | Mean number of disfluencies per sentence, including verbal and non-verbal edits, word repeats and restarts | Ability to formulate sentences, fluency in conversation |
| Non-verbal edits per turn | Mean number of non-verbal fillers (e.g., "uh", "ah", "hmm") per turn                                       | Speech fluency                                          |
| Verbal edits per turn     | Mean number of verbal fillers (e.g., "like", "I mean", "you know") per turn                                | Speech fluency                                          |
| Word repeats per turn     | Mean number of word repeats and stutters (e.g., "I, I, I'm going out") per turn                            | Speech fluency                                          |
| Restarts per turn         | Mean number of restarts (e.g., "did you call--phone him?") per turn                                        | Speech fluency                                          |

## How the tool works

This tool relies on TranscribeMe! transcripts to compute the metrics. The transcripts are expected to be in the following format:

```text
[Speaker 1]: <transcript>
[Speaker 2]: <transcript>
...
```

Additionally, verbatim transcripts are expected to follow a very specific style guide. This tool specifically uses the `TranscribeMe! Full Verbatim Style Guide 3.2`

Some of the key features of the style guide are:

- Only approved verbaim spellings for
  - Speech Fillers
  - Affirmatives and Negatives etc.,
- Word repeats / False starts will follow the convention `incomple-- incomplete word`
- Stuttering will be represented as `I-I-I am stuttering`
- Repetitions will be represented as `I, I, I am repeating`

### Stutering vs Repetitions

Stuttering is when a speaker repeats the same sound multiple times, e.g., "I-I-I am going out". Repetitions are when a speaker repeats the same word multiple times, e.g., "I, I, I am going out".
