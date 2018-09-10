<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- PAGE 404
                    ====================== -->
                    <div class="error-wrapper">
                    	<h1 class="error-title"><i class="fa fa-warning animated animated-infinite animated-dur-3 flash text-danger"></i> Request Not found</h1>
                    	<p class="lead">Oops! The requested page could not be found</p>

                    	<form action="" role="form">
                    		<div class="form-group">
                    			<div class="col-md-8 col-md-offset-2 input-group input-group-in">
	                    			<input type="text" class="form-control input-lg" placeholder="Search on Stilearn..." focus />
	                    			<span class="input-group-btn">
	                    				<button class="btn btn-lg btn-primary" type="submit">
											<i class="fa fa-search"></i>
										</button>
	                    			</span>
                    			</div>
                    		</div>
                    	</form><!--/form-->
                    </div><!--/error-wrapper-->