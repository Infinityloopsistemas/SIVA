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
                    	<h1 class="error-title"><i class="fa fa-cog fa-spin animated-dur-3 text-warning"></i> Internal Server Error</h1>
                    	<p class="lead">A generic error message, given when no more specific message is suitable</p>

                    	<form action="" role="form">
                    		<div class="form-group">
                    			<div class="col-md-8 col-md-offset-2 input-group input-group-in">
	                    			<input type="text" class="form-control input-lg" placeholder="Search on Stilearn..." />
	                    			<span class="input-group-btn">
	                    				<button class="btn btn-lg btn-primary" type="submit">
											<i class="fa fa-search"></i>
										</button>
	                    			</span>
                    			</div>
                    		</div>
                    	</form><!--/form-->
                    </div><!--/error-wrapper-->