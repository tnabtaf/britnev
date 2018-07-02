# britnev

Britnev, a meeting/conference Icebreaker program for generating icebreaker questionnaires for event participants.  Questions can be a mix of ones driven by participant characteristics and ones that aren't.  Generates forms and matching labels for event participants.

Reads a config file to determine which questions to generate.  Both types of questions are also defined there.

Participant information is read in from a TSV spreadsheet of participants.

This produces 

1. a list of pages that can be printed and then distributed to
    event participants.  Each page contains a different mix of questions on it.
    How often a particular question appears on different questionnaires is a
    function of the participant data, and the question definitions in the 
    config file.
    You can open this in a web browser and then save it to a PDF.
1. A spreadsheet of participant data that can be fed into a mail merge that 
    produces a column of mailing labels for each participant.  This more or
    less assumes that the number of labels for each participant is equal to
    the number of rows on the printed label sheet.
    This should be imported into a spreadsheet program like Excel, and then 
    used as a data source for a mail merge program such as Word.

The config file is JSON. See `config/britnev-config-example.json` for an example file.

## CONFIG FILE

Example:

```
  {
    "min_2b_tractable":   0.05,
    "max_2b_interesting": 0.30,
    "num_questions": 20,
    "label_columns": 4,
    "label_rows": 15,
    "labels_per_person": 15,
    "labels_fields": [
        "Last Name",
        "First Name",
        "Company",
        "Work City",
        "Work State",
        "Work Country"
    ],
    "questions": {
      {
        "question": "Who has attended at least 3 previous GCCs",
        "penetrance": 0.05,
        "difficulty": 1.0
      },
      {
        "question": "Who is here representing a different GCCBOSC sponsor",
        "penetrance": 1.0,
        "difficulty": 0.05
      },
     },
    "data_questions": {
      {
        "input_item": "Country",
        "input_arity": "Singleton"
        "output_question": "Someone from"
      },
      {
        "input_item": "Affiliations",
        "input_arity": "list",
        "output_question": "Someone affiliated with"
      },
  }
```

Explanation:

* Used with data-based questions.
  * `min_2b_tractable`:
    The minimum percentage of participants who need to have a particular value to ask that question.  For example if this is 0.05 and only 4% of your participants are from Germany, then it will **not** ask to find someone from Germany.

  * `max_2b_interesting`:
    The maximum percentage of participants who can have a particular value to ask that question.  For example, if this is 0.30 and 40% of attendees are from the US, then it will **not** ask to find someone from the US.

  * `label_columns`:
     How many columns will there be in each generated sheet of labels.

  * `label_rows`:
     How many rows of labels are on each sheet?

  * `labels_per_person`:
     How many labels to print per person.  This should probably always equal `label_columns or label_rows`.

  * `labels_fields`:
     List of columns from the participants spreadsheet that will be placed in the output labels spreadsheet. The values of these fields will eventually be printed on the generated labels

* `questions`:
  The list of questions that are not driven by participant data. Each question has these fields:
     * `question`:
       Full text of the question to ask.
     * `penetrance`:
       Floating point number between 0.00 and 1.00 that tells the program how often it should try to get the question in a questionnaire. There are two special values
       
       * 0.00: Do not include this question on any questionnaires.
       * 1.00: Include this question on every questionnaire.
     * `difficulty`:
       Floating point number between 0.05 and 1.00 that gives the program an estimate of how hard this question is to answer.  Difficulty is determined by two things:
         1. How hard is it to find out which other participants meet this criteria.  For example, it's easy to find who is presenting a poster.
         2. How hard is to then find someone who meets the criteria. For example, if there are only 4 poster presenters then it would be hard to get to them before everyone else does.

* `data_questions`:
    This list of questions that are driven by participant data.  Each question has these fields
    * `input_item`:
        Name of the column in the input spreadsheet that this question is based on.
    * `input_arity`:
        Is the value of the column a single value, or a list of values?
        Options are `Singleton` or `List`
    * `output_question`:
        The leading text of the question that will be generated from this input item.  For example
          `Someone from`
        would become
          `Someone from Germany`

    Penetrance and Difficulty are calculated for data questions, based on the actual data.  Item values that are rare have low penetrance and high difficulty.

# Customizing for your event

## Customizing your Config File

You can use this with any CSV file that has column headings.  All knowledge of the columns in the CSV is described in the config file. To run this, you will have to customize a config file for your inputs.  You also describe your questions and data driven questions in the config file.

## Customizing your forms

This program produces an HTML file that can then be saved as a PDF and printed.  The HTML contains two pages for each participant, meant to be printed back to back.  One page is instructions, and the other has questions.

The content and look and feel of this form is determined by, and is hard-coded in the `htmlforms.py` file.  You'll want to update this extensively to reflect the particulars of your event.  The default is the text we used for GCCBOSC 2018.

