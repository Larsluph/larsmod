<h1>Intro</h1>
Hi there! Here is where you can find examples and explanations to use this module perfectly!

<h2>Chronometer</h2>
This chronometer is pretty simple.<br/>
When you start it, it will return the actual system time. You just need to store this formatted time in a variable.<br/>
And when you stop it, it will return the actual time and the elapsed time between the start and now.<br/>

<h2>Decryptor</h2>
The decryptor (as said by his own name) can encrypt/decrypt simple cypher algorithms.<br/>
<p>For now, there are 2 algorithms :</p>
	<ul>
		<li><p>alpha - It converts a string into a digit list and vice versa.</p></li>
		<li><p>cesar - The Cesar algorithm takes a string and shifts all characters to a certain position.</p></li>
	</ul>

<h2>File Manager</h2>
<p>The File Manager is used to manage files (thanks Dr. Obvious). For now, the File Manager can only manage filenames.</p>
<p>You can remove the prefix or the suffix of multiple files in a given folder (sub-folders excluded) with the functions prefix_delete(path, prefix) and suffix_delete(path, suffix).</p>
<p>You can also remove the beginning of filenames with char_delete(path, char) that remove filenames up to the first occurrence of "char" (included) and char_nbr_delete(path, char_nbr) that remove filenames up to a certain "char_nbr".</p>

<h2>Utilities</h2>
<p>The utilities module is composed of some miscellaneous useful functions.</p>
<p>randomlistpicker(usrlist) return a random entry in the 'usrlist'.</p>
menu_generator(title, init, inputs, output) display a generated menu with a title, inputs and outputs.<br/>

<h2>Errors</h2>
	<ul>
		<li>TypeError - a function may return this error because an arguments' type isn't correct</li>
		<li>FileExistsError - a function in the file_manager may return this error because the modified file had the same name as an existing file</li>
		<li>InputError - char_delete may return this error because 'char' must be a single character</li>
	</ul>
