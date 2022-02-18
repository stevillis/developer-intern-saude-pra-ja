"""
<div id="main-splitpane-left" class="coding-question__left-pane"><section class="question-view__title-wrapper"><div class="beta-icon-editor beta-desc">BETA</div><span class="question-view__switch-theme__wrapper">Can’t read the text? <button class="ui-btn ui-btn-normal ui-btn-plain btn-as-link question-view__switch-theme"><div class="ui-content align-icon-right"><span class="ui-text" aria-hidden="false">Switch</span></div></button> theme</span><h1 class="question-view__title">1. Simple Max Difference</h1></section><section class="question-view__instruction"><div class="candidate-rich-text"><div id="ce03s3pr10t-instruction">
<style type="text/css">.ps-content-wrapper-v0 div { margin: 0 auto; overflow: auto; } .ps-content-wrapper-v0 div.preheader { display: none; } .ps-content-wrapper-v0 p { white-space: pre-wrap; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; } .ps-content-wrapper-v0 p.section-title { font-weight: bold; padding-bottom: 0px; } .ps-content-wrapper-v0 ol.plain-list, .ps-content-wrapper-v0 ul.plain-list { list-style-type: none; padding: 4px; } .ps-content-wrapper-v0 li { white-space: normal; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 code { color: black; } .ps-content-wrapper-v0 pre { background-color: #f4faff; border: 0; border-radius: 2px; margin: 8px; padding: 10px; } .ps-content-wrapper-v0 pre.scrollable-full-json { overflow-x: scroll; white-space: pre; } .ps-content-wrapper-v0 pre.scrollable-json { height: 300px; overflow-y: scroll; display: inline-grid; white-space: pre-wrap; padding-left: 8px; padding-right: 8px; padding-top: 4px; padding-bottom: 4px; } .ps-content-wrapper-v0 div.equation-parent { width: 400px; text-align: center; border: 1px solid #000; padding: 8px; } .ps-content-wrapper-v0 div.equation-parent.equation { width: 100%; display: inline-block; } .ps-content-wrapper-v0 figure { background-color: transparent; display: table; margin-top: 8px; margin-bottom: 8px; text-align: center; margin-left: auto; margin-right: auto; } .ps-content-wrapper-v0 figcaption { text-align: center; display: table-caption; caption-side: bottom; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 img { width: auto; max-width: 100%; height: auto; } .ps-content-wrapper-v0 details { background-color: transparent; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; } .ps-content-wrapper-v0 details details { padding-left: 8px; padding-right: 8px; } .ps-content-wrapper-v0 details summary { background-color: #39424e; color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px; } .ps-content-wrapper-v0 details details summary code { color: black; font-weight: bold; padding-left: 2px; padding-right: 2px; padding-top: 4px; padding-right: 4px; margin-left: 4px; } .ps-content-wrapper-v0 details div.collapsable-details { margin: 0 auto; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; overflow: auto; } .ps-content-wrapper-v0 details div.collapsable-details pre { margin-left: 4px; margin-right: 4px; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 table.normal { border: 1px solid black; border-collapse: collapse; border-color: darkgray; margin: 0 auto; margin-top: 8px; margin-bottom: 8px; padding: 8px; width: 96%; table-layout: fixed; } .ps-content-wrapper-v0 table.normal tbody { display: block; overflow-x: auto; overflow-y: hidden; } .ps-content-wrapper-v0 table.normal tbody tr:first-child th { font-weight: bold; white-space: normal; } .ps-content-wrapper-v0 table.normal tbody tr th, .ps-content-wrapper-v0 table.normal tbody tr td { font-weight: normal; white-space: nowrap; text-align: center; vertical-align: middle; border: 1px solid black; border-color: darkgray; padding: 8px; } .ps-content-wrapper-v0 table.database-table { border-collapse: collapse; border-color: darkgray; border: 1px solid black; width: auto; margin-left: 4px; margin-top: 8px; margin-bottom: 8px; padding: 8px; } .ps-content-wrapper-v0 table.database-table tbody { overflow-x: auto; overflow-y: hidden; border: none; } .ps-content-wrapper-v0 table.database-table tbody tr th, .ps-content-wrapper-v0 table.database-table tbody tr td { font-weight: normal; white-space: nowrap; text-align: center; vertical-align: middle; border: 1px solid black; border-color: darkgray; padding: 8px; } .ps-content-wrapper-v0 table.database-table tbody tr th { font-weight: bold; border: 1px solid black; } .ps-content-wrapper-v0 table.database-table tbody tr:nth-child(2) td { border: 1px solid black; } .ps-content-wrapper-v0 table.database-table tbody tr:nth-child(n+2) td:first-child { border-left-color: black; } .ps-content-wrapper-v0 table.database-table tbody tr:nth-child(n+2) td:last-child { border-right-color: black; } .ps-content-wrapper-v0 table.database-table tbody tr:last-child td { border-bottom-color: black; } .ps-content-wrapper-v0 table.database-table tbody tr td.description { text-align: left; white-space: pre-wrap; } .ps-content-wrapper-v0 table.normal tbody tr th.description { width: 60%; } .ps-content-wrapper-v0 table.function-params tbody tr:first-child td.headers { border-bottom-width: 2px; } .ps-content-wrapper-v0 table.function-params tbody tr:last-child td { border-top-width: 2px; border-top-color: darkgray; } .ps-content-wrapper-v0 table.function-params tbody tr td.headers { width: 25%; font-weight: bold; text-align: center; border: 1px solid black; border-right-width: 2px; border-color: darkgray; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell { width: 100%; height: 100%; padding: 0px; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table { width: 100%; height: 100%; padding: 0px; margin: 0px; border: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td.code { white-space: normal; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th { border-top: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th:first-child { border-left: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th:last-child { border-right: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr:last-child td { border-bottom: 0; border-top-width: 1px; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td:first-child { border-left: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td:last-child { border-right: 0; } .ps-content-wrapper-v0 table.sudoku { border-collapse: collapse; border-color: darkgray; margin: 0 auto; margin-top: 8px; margin-bottom: 8px; padding: 8px; } .ps-content-wrapper-v0 table.sudoku colgroup, tbody { border: 3px solid black; } .ps-content-wrapper-v0 table.sudoku td { border: 1px solid black; height: 25px; width: 25px; text-align: center; padding: 0; } .ps-content-wrapper-v0 .left { text-align: left; } .ps-content-wrapper-v0 .right { text-align: right; } .ps-content-wrapper-v0 .code { font-family: monospace; white-space: nowrap; } .ps-content-wrapper-v0 .json-object-array ol, .ps-content-wrapper-v0 .json-object-array ol ul { margin-top: 0px; padding-left: 14px; } .json-object-array li { float: left; margin-right: 30px; margin-left: 10px; } .json-object-array pre { padding: 4px; margin-left: 0px; }
</style>

<div class="ps-content-wrapper-v0">






<p>In securities research, an analyst will look at a number of attributes for a stock. One analyst would like to keep a record of the highest positive spread between a closing price and the closing price on any prior day in history. Determine the maximum positive spread for a stock given its price history. If the stock remains flat or declines for the full period, return -1.</p>

<p>&nbsp;</p>

<p><strong>Example 0</strong></p>

<p><em>px = [7, 1, 2, 5]</em></p>

<p>&nbsp;</p>

<p>Calculate the positive difference between each price and its predecessors:</p>

<ul>
	<li>At the first quote, there is no earlier quote&nbsp;to compare to.</li>
	<li>At the second quote, there was no earlier price that was lower.</li>
	<li>At the third quote, the price is higher than the second quote:
	<ul>
		<li>2 - 1 = 1</li>
	</ul>
	</li>
	<li>For the fourth quote, the price is higher&nbsp;than the third and the second quotes:
	<ul>
		<li>5 - 2 = 3</li>
		<li>5 - 1 = 4.</li>
	</ul>
	</li>
	<li>The maximum difference is 4.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1</strong></p>

<p><em>px = [7, 5, 3, 1]</em></p>

<p>&nbsp;</p>

<ul>
	<li>The price declines each quote, so there is never a difference greater than 0.&nbsp; In this case, return -1.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Function Description </strong></p>

<p>Complete the function <em>maxDifference</em> in the editor below.</p>

<p>&nbsp;</p>

<p><em>maxDifference&nbsp;</em>has the following parameters:</p>

<p>&nbsp; &nbsp; <em>int px[n]:</em>&nbsp;an array of stock prices (quotes)</p>

<p>Returns:</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;<em>int:</em>&nbsp; the maximum difference between two prices as described above</p>

<p>&nbsp;</p>

<p class="section-title">Constraints</p>

<ul>
	<li><em>1&nbsp;≤ n ≤&nbsp;10<sup>5</sup></em></li>
	<li>
<em>-10<sup>5</sup> ≤ px[i]</em><em>&nbsp;</em><em>≤&nbsp;10<sup>5</sup></em>
</li>
</ul>

<p>&nbsp;</p>
<!--       <StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details><summary class="section-title">Input Format For Custom Testing</summary>

<div class="collapsable-details">
<p>Locked stub code reads input from stdin and passes it to the function.</p>

<p>&nbsp;</p>

<p>The first line contains an integer, <em>n</em>, denoting the number of elements in the array <em>px.</em></p>

<p>Each of the next <em>n&nbsp;</em>lines contains an integer, <em>px[i]</em>.</p>
</div>
</details>
<!--        </StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details open="open"><summary class="section-title">Sample Case 0</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input For Custom Testing</p>

<pre>STDIN&nbsp;&nbsp;&nbsp;&nbsp;Function
-----&nbsp;&nbsp;&nbsp;&nbsp;--------
7&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;px[] size n = 7
2&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;px = [2, 3, 10, 2, 4, 8, 1]
3
10
2
4
8
1
</pre>

<p class="section-title">Sample Output</p>

<pre>8
</pre>

<p class="section-title">Explanation</p>

<p class="section-title">&nbsp;</p>

<p>Calculate the positive difference between each price quote and the previous ones :</p>

<ul>
	<li>There is no predecessor for the first quote.</li>
	<li>At the second quote, the price is higher than the first&nbsp;quote:
	<ul>
		<li><em>px[1] - px[0] = 3 - 2 = 1</em></li>
	</ul>
	</li>
	<li>At the third quote, the price is higher than the first and second quotes:
	<ul>
		<li><em>px[2] - px[1] = 10 - 3&nbsp;= 7</em></li>
		<li><em>px[2] - px[0] = 10 - 2&nbsp;= 8</em></li>
	</ul>
	</li>
	<li>At the fifth quote, the price is higher than the first and second quotes:&nbsp;
	<ul>
		<li><em>px[4] - px[1] = 4 - 3 = 1</em></li>
		<li><em>px[4] - px[0] = 4 - 2 = 2</em></li>
	</ul>
	</li>
	<li>At the sixth quote, the price is higher than the first, second, fourth and fifth&nbsp;quotes:&nbsp;
	<ul>
		<li><em>px[5] - px[0] = 8 - 2=6</em></li>
		<li><em>px[5] - px[1] = 8 - 3=5</em></li>
		<li><em>px[5] - px[3] = 8 - 2=6</em></li>
		<li><em>px[5] - px[4] = 8 - 4=4</em></li>
	</ul>
	</li>
	<li>The maximum difference is 8.</li>
</ul>

<p>&nbsp;</p>
</div>
</details>

<details open=""><summary class="section-title">Sample Case 1</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input For Custom Testing</p>

<pre>STDIN&nbsp;&nbsp;&nbsp;&nbsp;Function
-----&nbsp;&nbsp;&nbsp;&nbsp;--------
6&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;px[] size n = 6
7&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;px = [7, 9, 5, 6, 3, 2]
9
5
6
3
2</pre>

<p class="section-title">Sample Output</p>

<pre>2

</pre>

<p class="section-title">Explanation</p>

<p class="section-title">&nbsp;</p>

<p>Calculate the positive difference between each quote and the previous ones :</p>

<ul>
	<li>The second quote, the price is higher than the first:
	<ul>
		<li><em>px[1] - px[0] = 9 - 7 = 2</em></li>
	</ul>
	</li>
	<li>After that,&nbsp;the prices decline steadily.</li>
	<li>The maximum difference is 2.</li>
</ul>

<p>&nbsp;</p>
</div>
</details>
</div>
</div></div></section></div>s
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY px as parameter.
#

def maxDifference(px):
    # Write your code here
    previous_values_list = []
    max_difference = -1
    for pos, value in enumerate(px):
        previous_values_list.append(value)
        if pos > 0:
            for value_prev in previous_values_list:
                if value > value_prev:
                    difference = value - value_prev
                    if difference > max_difference:
                        max_difference = difference

    return max_difference


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #px_count = int(input().strip())

    #px = []

    # for _ in range(px_count):
    #    px_item = int(input().strip())
    #    px.append(px_item)

    # ----- testes -----
    # px = [7, 1, 2, 5]
    # px = [7, 5, 3, 1]
    # px = [2, 3, 10, 2, 4, 8, 1]
    px = [6, 7, 9, 5, 6, 3, 2]
    # ----- /testes -----
    result = maxDifference(px)
    print(result)

    #fptr.write(str(result) + '\n')

    # fptr.close()
