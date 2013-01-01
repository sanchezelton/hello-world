<html>
<head>
<title>Hello Data Types!</title>
</head>
<body>
<?php
echo ("<h1>Hello Data Types!</h1><p>");
$Variable = "This is some text";
echo ("&quot;$Variable&quot; is a variable of type: ");
print (gettype($Variable));
echo ("<p>");

$first_int = 5;
$second_int = 2;
$quotient = $first_int / $second_int;
$answerIsValid = TRUE;
$booleanType = gettype($answerIsValid);
echo ("If we divide $first_int by $second_int, we get $quotient. ");
echo ("This is a true answer, but PHP returns a $answerIsValid for a $booleanType.<p>");

$str = <<<ENDQUOTE
	This is a multiline string.
	Note that I don't have to escape any "quotes" here.
ENDQUOTE;
echo ($str);
?>

<!-- Code Explanation -->


<hr>
<h4>Code:</h4>
<PRE>
&lt;?php
echo ("&lt;h1&gt;Hello Data Types!&lt;/h1&gt;&lt;p&gt;");
$Variable = "This is some text";
echo ("&quot;$Variable&quot; is a variable of type: ");
print (gettype($Variable));
echo ("&lt;p&gt;");

$first_int = 5;
$second_int = 2;
$quotient = $first_int / $second_int;
$answerIsValid = TRUE;
$booleanType = gettype($answerIsValid);
echo ("If we divide $first_int by $second_int, we get $quotient");
echo ("This is a true answer, but PHP returns a $answerIsValid for a $booleanType.&lt;p^gt;");

$str = &lt;&lt;&lt;ENDQUOTE
	This is a multiline string.
	Note that I don't hae to escape any &quot;quotes&quot; here.
ENDQUOTE;
echo ($str);
?&gt;
</PRE>

</body>
</html>