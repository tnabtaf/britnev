#!/usr/local/bin/python3
#
# Question list / form in HTML Format.
#

# Instructions should be printed on the back of each page.

# 1.75" x 0.666 Probable label size?
DOCUMENT_HEADER = """
<html>
<head>
<style>
  * {
   font-family: Helvetica, sans-serif;
  }
  h2 {
    text-align: center;
    margin: 0;
  }
  .answer-box {
    height: 0.72in;
    width: 2.5in;
    border: 1px solid grey;
  }
  .question {
    border: none;
    text-align: right;
  }
  table {
    width: 100%;
  }
  td {
    vertical-align: top;
    font-size: 12pt;
    padding: 0.5em 1em;
  }
  table {
    border-spacing: 0;
  }
  @media print {
    footer {page-break-after: always;}
  }
</style>
</head>
<body>
"""

PAGE_BREAK = """
<footer></footer>
"""

QUESTION_PAGE_HEADER = """
<table style="width:100%; font-size: larger;">
 <tr>
   <td>Your name</td>
 </tr>
</table>
"""

INSTRUCTIONS = """
<div style='font-size: larger'>

<h2>Break Some Ice @ GCCBOSC 2018</h2>

<br />

<div style="float: left"><br />
  <img
    src="gccbosc-logo-bw.png" width="100"
    style="padding: 0 5 5 0; margin: 0 5 5 0; border: 1 gray solid" />
</div>

<p>GCCBOSC will be larger than any BOSC or GCC before it. This is good
 because it will create more opportunities to learn from each other and
 to create collaborations. However, it can also be daunting: The bigger
 the meeting, the harder it is to maintain the interactive and collaborative
 feel that past BOSCs and GCCs have successfully cultivated. So, to address
 this...</p>

<br />

<h2>We are pleased to offer the first ever GCCBOSC Icebreaker</h2>

<p>The Icebreaker is generously sponsored by <strong>Advanced HPC</strong>.
 There will be one winner, drawn at random from all forms with the maximum
 number of correct answers (whatever the maximum number is), and that winner
 will receive an <strong>Oculus Rift VR System provided by Advanced
 HPC</strong>.  That's a $400 value.</p>

<p>Advanced HPC offers expert advice, customization, and consultation for
 your high-performance computing needs.  As HPC software specialists, our
 engineers can customize complex solutions for you more quickly and
 efficiently than our competitors. </p>
</div>

<h1>Instructions</h1>

<div style="float: right; style="padding: 0 0 10 10"">
<img src="RiftTrimmed3.jpg" width="300" />
</div>

<ol>
<li> Find a different person for each question in your list. </li>
<li> Convince them to give you one of their stickers.  You may have to trade
  one of your stickers, or information, or engage in outright bribery.</li>
<li> You <em>may not use</em> one of your stickers to answer one of your
  questions.</li>
<li> Only official conference stickers will be recognized. </li>
<li> Once you have given away all of your stickers, you won't get any
  more.</li>
<li> <em>You lose major style points if you engage with someone, and the
 only thing you get is one of their stickers.</em>  Engage! Find out what
 they do, what their challenges are, ... </li>
<li> Sponsors and conference organizers are <em>not eligible</em> for the
 prize, although we do have stickers. </li>
<li> <strong>Have fun, meet people, build new collaborations, expand your
 network, and go outside your comfort zone!</strong></li>
</ol>

<br />

<h2>The Drawing</h2>

<p>There will be a drawing for the prize during the last session of the
 conference on Thursday.</p>
<p> Things to know:
<ol>
<li> <strong>Your form needs to be turned in to the conference desk no
 later than the 1:40 PM on Thursday</strong> (the start of session 7).
 Forms turned in after that will not be eligible. </li>
<li> Forms will be reviewed by the organizers.
<li> All forms with the maximum number of correct answers (whatever the
 maximum number is) will be entered in the prize drawing. </li>
<li> The prize drawing will happen at the conclusion of the conference,
 at the end of Session 8.</li>
<li><strong> You must be present at the drawing to win.</strong>
</ol>

<br />
<div style="text-align: center">
<img src="ahpc-logo-bw.png" width="450" style="padding: 0 0 5 5"/>
</div>


"""


class QuestionPage:
    """
    Defines pages that list the questions.
    """

    def __init__(self, question_list):
        """Given a question list, create a QuestionPage.
        Later this will be rendered.
        """
        self.questions = question_list

        return None

    def to_html(self, question_limit):
        """
        Render this question page as HTML and return the text as text.
        Generate no more than question_limit questions per page.

        Pages consist of
          Header section
          question list
          Closing section

        This does not generate the surrounding HTML document.
        It does generate a page break at the end.
        """
        html = []                         # converted to 1 string at end
        html.append("<h2>Break Some Ice @ GCCBOSC 2018</h2>")
        html.append("<hr />")

        html.append("<p>Find someone who...<br /></p>")
        html.append("<table>")
        i = 1
        for q in self.questions:
            html.append(" <tr>")
            html.append("  <td> {0}.</td>".format(i))
            html.append("  <td class='question'> {0}</td>".format(q.text))
            html.append("  <td class='answer-box'> </td>")
            html.append(" </tr>")
            i += 1
            if i > question_limit:
                break

        html.append("</table>")
        html.append("<hr />")
        html.append("<h3>Your Name:</h3>")

        html.append(PAGE_BREAK)

        return("\n".join(html))


class Forms:
    """
    The output document.
    """

    def __init__(self, num_questions):
        """
        Create a document that is ready to have forms and instructions
        added to it.  Limit the number of questions on each form to
        num_questions max.
        """
        self.question_pages = []
        self.question_limit = num_questions
        return None

    def add_new_form(self, question_list):
        """
        Add a new form, complete with questions and instructions to
        the document.

        """
        self.question_pages.append(QuestionPage(question_list))
        return None

    def to_html(self):
        """
        Convert the form document to HTML.
        """
        self.html = []
        self.html.append(DOCUMENT_HEADER)
        for qp in self.question_pages:
            self.html.append(qp.to_html(self.question_limit))
            self.html.append(INSTRUCTIONS)
            self.html.append(PAGE_BREAK)

        return("\n".join(self.html))
