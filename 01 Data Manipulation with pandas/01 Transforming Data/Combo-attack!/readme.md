## Combo-attack!

You've seen the four most common types of data manipulation: sorting rows, subsetting columns, subsetting rows, and adding new columns. In a real-life data analysis, you can mix and match these four manipulations to answer a multitude of questions.

In this exercise, you'll answer the question, "Which state has the highest number of homeless individuals per 10,000 people in the state?" Combine your new `pandas` skills to find out.

<hr>

**Instructions**
* Add a column to `homelessness`, `indiv_per_10k`, containing the number of homeless individuals per ten thousand people in each state.
* Subset rows where `indiv_per_10k` is higher than 20, assigning to high_homelessness.
* Sort `high_homelessness` by descending `indiv_per_10k`, assigning to `high_homelessness_srt`.
* Select only the state and `indiv_per_10k` columns of `high_homelessness_srt` and save as result. *Look at the `result`*.

> **script.py**
> ```
> # Create indiv_per_10k col as homeless individuals per 10k state pop
> homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]
>
> # Subset rows for indiv_per_10k greater than 20
> high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]
>
> # Sort high_homelessness by descending indiv_per_10k
> high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)
>
> # From high_homelessness_srt, select the state and indiv_per_10k cols
> result = high_homelessness_srt[["state", "indiv_per_10k"]]
>
> # See the result
> print(result)
> ```
>
> **Output**
> ```
>                    state  indiv_per_10k
> 8   District of Columbia         53.738
> 11                Hawaii         29.079
> 4             California         27.624
> 37                Oregon         26.636
> 28                Nevada         23.314
> 47            Washington         21.829
> 32              New York         20.392
> ```