"""
<div id="main-splitpane-left" class="coding-question__left-pane"><section class="question-view__title-wrapper"><div class="beta-icon-editor beta-desc">BETA</div><span class="question-view__switch-theme__wrapper">Can’t read the text? <button class="ui-btn ui-btn-normal ui-btn-plain btn-as-link question-view__switch-theme"><div class="ui-content align-icon-right"><span class="ui-text" aria-hidden="false">Switch</span></div></button> theme</span><h1 class="question-view__title">2. Python: Alphabet Filter</h1></section><section class="question-view__instruction"><div class="candidate-rich-text"><div id="br74e2h9lgk-instruction"><style type="text/css">.ps-content-wrapper-v0 div { margin: 0 auto; overflow: auto; }
.ps-content-wrapper-v0 div.preheader { display: none; }
.ps-content-wrapper-v0 p { white-space: pre-wrap; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; }
.ps-content-wrapper-v0 p.section-title { font-weight: bold; padding-bottom: 0px; }
.ps-content-wrapper-v0 ol.plain-list, .ps-content-wrapper-v0 ul.plain-list { list-style-type: none; padding: 4px; }
.ps-content-wrapper-v0 li { white-space: normal; margin-top: 4px; margin-bottom: 4px; }
.ps-content-wrapper-v0 code {color: black; background: transparent; font-weight: normal; font-size: 1em; }
.ps-content-wrapper-v0 pre { background-color: #f4faff; border: 0; border-radius: 2px; margin: 8px; padding: 10px; }
.ps-content-wrapper-v0 figure { background-color: transparent; display: table; margin-top: 8px; margin-bottom: 8px; text-align: center; margin-left: auto; margin-right: auto; }
.ps-content-wrapper-v0 figcaption { text-align: center; display: table-caption; caption-side: bottom; margin-top: 4px; margin-bottom: 4px; }
.ps-content-wrapper-v0 img { width: auto; max-width: 100%; height: auto; }
.ps-content-wrapper-v0 details { background-color: transparent; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; }
.ps-content-wrapper-v0 details summary { background-color: #39424e; color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px; }
.ps-content-wrapper-v0 details div.collapsable-details { margin: 0 auto; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; overflow: auto; }
.ps-content-wrapper-v0 details div.collapsable-details pre { margin-left: 4px; margin-right: 4px; margin-top: 4px; margin-bottom: 4px; }
.ps-content-wrapper-v0 table { border: 1px solid black; border-collapse: collapse; border-color: darkgray; margin: 0 auto; margin-top: 8px; margin-bottom: 8px; padding: 8px; width: 96%; table-layout: fixed; }
.ps-content-wrapper-v0 table tbody tr th, .ps-content-wrapper-v0 table tbody tr td { font-weight: bold; white-space: nowrap; text-align: center; vertical-align: middle; border: 1px solid black; border-color: darkgray; padding: 8px; }
.ps-content-wrapper-v0 table tbody tr th.description { width: 60%; }
.ps-content-wrapper-v0 table tbody tr td { font-weight: normal; white-space: normal; }
.ps-content-wrapper-v0 table.function-params tbody tr:first-child td.headers { border-bottom-width: 2px; }
.ps-content-wrapper-v0 table.function-params tbody tr:last-child td { border-top-width: 2px; border-top-color: darkgray; }
.ps-content-wrapper-v0 table.function-params tbody tr td.headers { width: 25%; font-weight: bold; text-align: center; border: 1px solid black; border-right-width: 2px; border-color: darkgray; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell { width: 100%; height: 100%; padding: 0px; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table { width: 100%; height: 100%; padding: 0px; margin: 0px; border: 0; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td.code { white-space: normal; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th { border-top: 0; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th:first-child { border-left: 0; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th:last-child { border-right: 0; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr:last-child td { border-bottom: 0; border-top-width: 1px; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td:first-child { border-left: 0; }
.ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td:last-child { border-right: 0; }
.ps-content-wrapper-v0 .left { text-align: left; }
.ps-content-wrapper-v0 .right { text-align: right; }
.ps-content-wrapper-v0 .code { font-family: monospace; white-space: nowrap; }
.ps-content-wrapper-v0 .json-object-array ol, .ps-content-wrapper-v0 .json-object-array ol ul { margin-top: 0px; padding-left: 14px; }
.json-object-array li { float: left; margin-right: 30px; margin-left: 10px; }
.json-object-array pre { padding: 4px; margin-left: 0px; }
</style>
<div class="ps-content-wrapper-v0">
<p>Given a string consisting of only lowercase characters, create two methods that remove all the consonants or vowels from the given word. They must retain the original order of the characters in the returned strings.</p>

<p><em>Example:</em></p>

<p><em>s = '<b>onomatopoeia</b></em>'</p>

<ul>
	<li>The <em>filter_vowels</em>&nbsp;method removes all vowels from <em>s</em>&nbsp;and returns the string '<b><em>nmtp</em>'.</b>
</li>
	<li>The <em>filter_consonants</em>&nbsp;method removes all consonants from <em>s</em> and returns the string '<b><em>ooaooeia</em>'.</b>
</li>
</ul>

<p>&nbsp;</p>

<p class="section-title">Function Description</p>

<ul>
</ul>

<p>&nbsp;</p>

<p>For a given definition of a class <em>LetterFilter</em>, complete its methods <em>filter_vowels</em> and <em>filter_consonants</em>. The class takes a string in the constructor and stores it to its <em>s</em>&nbsp;attribute. The method <em>filter_vowels</em> must return a new string with all vowels removed from it. Similarly, the method <em>filter_consonants</em> must return a new string with all consonants removed from it.</p>

<p>&nbsp;</p>

<p class="section-title">Constraints</p>

<ul>
	<li>The string contains only lowercase letters in the range ascii[a-z]</li>
	<li>The string contains at least one vowel and at least one consonant</li>
</ul>

<p>&nbsp;</p>
<!-- <StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details><summary class="section-title">Input Format For Custom Testing</summary>

<div class="collapsable-details">
<p>The first line contains a string, <em>s</em>, that denotes the string to be transformed.</p>
</div>
</details>
<!-- </StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details open="open"><summary class="section-title">Sample Case 0</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input 0</p>

<pre>STDIN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Function
-----&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--------
hackerrank →&nbsp;string s = 'hackerrank'</pre>

<p class="section-title">Sample Output 0</p>

<pre>hckrrnk
aea</pre>

<p class="section-title">Explanation 0</p>

<ul>
	<li>The first result is after removing all vowels, {a, e, i, o, u}, from the string.</li>
	<li>The second result is after removing all consonants.</li>
</ul>
</div>
</details>

<details><summary class="section-title">Sample Case 1</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input 1</p>

<pre>STDIN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Function
-----&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  --------
programming →  string s = 'programming'
</pre>

<p class="section-title">Sample Output 1</p>

<pre>prgrmmng
oai</pre>

<p class="section-title">Explanation 1</p>

<ul>
	<li>The first result is after removing all vowels, {a, e, i, o, u}, from the string.</li>
	<li>The second result is after removing all consonants.</li>
</ul>
</div>
</details>
</div>
</div></div></section></div>
"""


class LetterFilter:

    def __init__(self, s):
        self.s = s
        self.list_voews = ['a', 'e', 'o', 'i', 'o', 'u']
        self.list_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                                'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


# Enter your code here.
# Complete the classes below.
# Reading the inputs and writing the outputs are already done for you.
#
# class LetterFilter:
#
#   def __init__(self, s):
#       self.s = s

    def filter_vowels(self):
        # Enter your code here
        # Return a string
        custom_s = []
        for letter in self.s:
            if letter in self.list_voews:
                custom_s.append('')
            else:
                custom_s.append(letter)
        return ''.join(custom_s)

    def filter_consonants(self):
        # Enter your code here
        # Return a string
        custom_s = ['']
        for letter in self.s:
            if letter in self.list_consonants:
                custom_s.append('')
            else:
                custom_s.append(letter)
        return ''.join(custom_s)


# s = input()
#---- test
s = 'onomatopeia'
# ---- /test
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())
