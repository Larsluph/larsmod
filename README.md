<h1>Intro</h1>
Hi there! Here is where you can find examples and explanations to use this module perfectly!

<h6>WARNING<br/>This module is written for Windows in Python3. Some things could not work properly.</h6>

<h1>Chronometer</h1>
This chronometer is pretty simple.<br/>
When you start it, it will return the actual system time. You just need to store this formatted time in a variable.<br/>
And when you stop it, it will return the actual time and the elapsed time between the start and now.<br/>

<h1>Decryptor</h1>
The decryptor (as said by his own name) can encrypt and decrypt simple cypher algorithms.<br/>
<p>For now, there are 4 algorithms :</p>
<ul>
	<li>alpha - It converts a string into a digit list and vice versa.</li>
	<li>cesar - The cesar algorithm takes a string and shifts all characters to a certain position.</li>
	<li>morse - It enables to translate morse code into letters and vice versa.</li>
	<li>Numpad - ONLY ABLE TO CYPHER (for now) - convert a text string to a digit string.</li>
</ul>

<h1>File Manager</h1>
<p>The File Manager is used to manage files (thanks Captain Obvious). For now, the File Manager can only manage filenames.</p>
<ul>
	<li>You can remove the prefix or the suffix of multiple files in a given folder (sub-folders excluded) with the functions prefix_delete(path, prefix) and suffix_delete(path, suffix).</li>
	<li>You can also remove the beginning of filenames with char_delete(path, char) that remove filenames up to the first occurrence of "char" (included) and char_nbr_delete(path, char_nbr) that remove filenames up to a certain "char_nbr".</li>
</ul>

<h1>Utilities</h1>
<p>The utilities module is composed of some miscellaneous useful functions.</p>
<ul>
	<li>randomlistpicker(usrlist) return a random entry in the 'usrlist'.</li>
	<li>letter_randomizer(words) take all characters in a string (single word / sentence) or in a list of words and randomize them to return an "anagram"</li>
	<li>now() return a list with [day name, day number, month name, year, hour, minute, second]</li>
	<li>menu_generator(title, init, inputs, output) display a generated menu with a title, inputs and outputs.</li>
	<li>math_calc.launch() enables to launch a python calculator console (works in radians)</li>
	<li>time_calc.launch() enables to launch a python calculator console that calculate time</li>
</ul>

<h1>Errors</h1>
	<ul>
		<li>TypeError - a function may return this error because an arguments' type isn't correct</li>
		<li>FileExistsError - a function in the file_manager may return this error because the modified file had the same name as an existing file</li>
		<li>InputError - char_delete may return this error because 'char' must be a single character</li>
	</ul>
