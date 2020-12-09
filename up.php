<?php 

$name= $_FILES['file']['name'];

$tmp_name= $_FILES['file']['tmp_name'];

$position= strpos($name, ".");

$fileextension= substr($name, $position + 1);

$fileextension= strtolower($fileextension);


if (isset($name)) {

$path= 'uploads/';
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
											     	echo 'Uploaded!';
												shell_exec('python imageExtracter.py');
												shell_exec('python PrepareBlockChain.py');

										  	     }
				}
			}
}
?>
<script type="text/javascript">location.href = 'uploadVerification.html';</script>
