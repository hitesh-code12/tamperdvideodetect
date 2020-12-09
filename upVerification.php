<body style="background-image: url('bg.jpeg');">
<center>

<h2>Original video: </h2> 
<br>
<video width="320" height="240" controls>
  <source src="uploads/sample.mp4" type="video/mp4">
 </video>
<br>
<h2>Verification video:</h2> 
<br>
<video width="320" height="240" controls>
  <source src="verificationUpload/sample.mp4" type="video/mp4">
 </video>
<br>
</center>
</body>
<?php 

$name= $_FILES['file']['name'];

$tmp_name= $_FILES['file']['tmp_name'];

$position= strpos($name, ".");

$fileextension= substr($name, $position + 1);

$fileextension= strtolower($fileextension);


if (isset($name)) {

$path= 'verificationUpload/';
if (empty($name))
{
	echo "Please choose a file";
}
else if (!empty($name)){
				if (($fileextension !== "mp4") && ($fileextension !== "ogg") && ($fileextension !== "webm"))
				{
					echo "The file extension must be .mp4, .ogg, or .webm in order to be uploaded";
				}


				else if (($fileextension == "mp4") || ($fileextension == "ogg") || ($fileextension == "webm"))
				{
					if (move_uploaded_file($tmp_name, $path."sample.mp4")) 
											     {
											     	
												shell_exec('python imageExtracterVerification.py');
												echo '<br><br><br><h1> Result  :'.shell_exec('python verify.py').'</h1>';

										  	     }
					else{
								echo 'Uploaded Failed!';
						}
				}
			}
}
?>
</body>
