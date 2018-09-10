<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Stilearn Admin Bootstrap</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="stilearning">

        <meta http-equiv="x-pjax-version" content="v173">

        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
        <!-- fav and touch icons -->
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="ico/favico-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="ico/favico-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="ico/favico-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="ico/favico-57-precomposed.png">
        <link rel="shortcut icon" href="ico/favico.png">
        <link rel="shortcut icon" href="ico/favico.ico">

        <!-- build:css styles/vendor.css -->
        <!-- bower:css -->
        <link rel="stylesheet" href="bower_components/bootstrap/dist/css/bootstrap.css">
        <link rel="stylesheet" href="bower_components/font-awesome/css/font-awesome.css">
        <link rel="stylesheet" href="bower_components/animate.css/animate.css">
        <link rel="stylesheet" href="bower_components/Hover/css/hover.css">
        <!-- endbower -->
        <!-- endbuild -->
        
        <!-- build:css(.tmp) styles/main.css -->
        <link id="style-components" href="styles/loaders.css" rel="stylesheet">
        <link id="style-components" href="styles/bootstrap-theme.css" rel="stylesheet">
        <link id="style-components" href="styles/dependencies.css" rel="stylesheet">
        <link id="style-base" href="styles/stilearn.css" rel="stylesheet">
        <link id="style-responsive" href="styles/stilearn-responsive.css" rel="stylesheet">
        <link id="style-helper" href="styles/helper.css" rel="stylesheet">
        <link id="style-sample" href="styles/pages-style.css" rel="stylesheet">
        <!-- endbuild -->
        
        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
          <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7/html5shiv.min.js"></script>
        <![endif]-->
    </head>

    <body class="animated fadeIn">		

		<div class="content content-full">
			<div class="container">
				<div class="signin-wrapper">
					<div class="tab-content">
						<div class="row tab-pane fade in active" id="signin">
							<div class="col-md-offset-1 col-md-6 hidden-sm hidden-xs">
								<div id="carousel-example" class="carousel slide" data-ride="carousel">
							      	<ol class="carousel-indicators">
								        <li data-target="#carousel-example" data-slide-to="0" class="active"></li>
								        <li data-target="#carousel-example" data-slide-to="1"></li>
								        <li data-target="#carousel-example" data-slide-to="2"></li>
								        <li data-target="#carousel-example" data-slide-to="3"></li>
								        <li data-target="#carousel-example" data-slide-to="4"></li>
							      	</ol>
							      	<div class="carousel-inner">
								        <div class="item active">
								          	<img src="images/dummy/img7.png" alt="Slide image">
								        </div>
								        <div class="item">
								          	<img src="images/dummy/img11.png" alt="Slide image">
								        </div>
								        <div class="item">
								          	<img src="images/dummy/img2.png" alt="Slide image">
								        </div>
								        <div class="item">
								          	<img src="images/dummy/img6.png" alt="Slide image">
								        </div>
								        <div class="item">
								          	<img src="images/dummy/img3.png" alt="Slide image">
								        </div>
							      	</div>
							      	<a class="left carousel-control" href="#carousel-example" data-slide="prev">
							        	<span class="glyphicon glyphicon-chevron-left"></span>
							      	</a>
							      	<a class="right carousel-control" href="#carousel-example" data-slide="next">
							        	<span class="glyphicon glyphicon-chevron-right"></span>
							      	</a>
							    </div>
							</div><!--/cols-->

							<div class="col-md-offset-1 col-md-4 col-sm-offset-2 col-sm-8">							
								<div class="signin">
									<div class="signin-brand">
										<a href="page-signin.php">
											<img class="lazy" data-original="images/dummy/stilearn-logo-primary.png" alt="Sign In">
										</a>
									</div><!--/signin-brand-->

									<form action="index.php" method="POST" data-validate="form" role="form" id="signin-form">
										<p><small>Stilearn Admin account. <a href="#">Learn more?</a></small></p>
										<div class="form-group">
											<div class="input-group input-group-in">
												<span class="input-group-addon text-muted">@</span>
												<input type="text" class="form-control" name="username" required minlength="4" placeholder="johndoe" autocomplete="off">
											</div><!--/input-group-->
										</div><!--/form-group-->

										<div class="form-group">
											<div class="input-group input-group-in">
												<span class="input-group-addon text-muted"><i class="fa fa-circle-o"></i></span>
												<input type="password" class="form-control" name="password" required minlength="4" placeholder="Password">
											</div><!--/input-group-->
										</div><!--/form-group-->

										<div class="form-group">
											<div class="nice-checkbox">
												<input class="checkbox-o" type="checkbox" name="keep-signin" id="keep-signin"/>
												<label for="keep-signin">Keep me sign in</label>
											</div>
										</div><!--/form-group-->

										<div class="form-group form-actions">
											<input type="submit" class="hidden-sm btn btn-primary" value="Sign In">
											<input type="submit" class="visible-sm btn btn-lg btn-block btn-primary" value="Sign In">
										</div><!--/form-group-->

										<p>
											<small>
												<a href="#modalRecover" data-toggle="modal">Can't Access your Account?</a><br>
												<a href="#" class="hidden-sm">Sign in with another account?</a>
											</small>
										</p>
										<p class="hidden-sm">
											<a href="#" rel="tooltip" title="Signin with Twitter account" class="btn btn-sm btn-info"><span class="fa fa-twitter"></span></a>
											<a href="#" rel="tooltip" title="Signin with Google account" class="btn btn-sm btn-danger"><span class="fa fa-google-plus"></span></a>
											<a href="#" rel="tooltip" title="Signin with Github account" class="btn btn-sm btn-cloud"><span class="fa fa-github"></span></a>
										</p>

										<p class="margin-top"><small>Don't have a account? <a data-toggle="tab" href="#signup"><strong>Creata an Account</strong></a></small></p>
									</form><!--/#signin-form-->
								</div><!--/signin-->


								<!-- modalRecover -->
	                            <div class="modal fade" id="modalRecover" tabindex="-1" role="dialog" aria-labelledby="modalRecoverLabel" aria-hidden="true">
	                                <div class="modal-dialog">
	                                    <div class="modal-content">
	                                        <div class="modal-header">
	                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
	                                            <h4 class="modal-title" id="modalRecoverLabel">Reset Password</h4>
	                                        </div>
	                                        <div class="modal-body">
	                                            <form action="index.php" method="POST" data-validate="form" role="form" id="recover-form">
													<div class="form-group">
														<div class="input-group input-group-in">
															<span class="input-group-addon text-muted">@</span>
															<input type="email" class="form-control" name="recover" required autocomplete="off">
														</div><!--/input-group-->
													</div><!--/form-group-->
													<p class="text-muted"><small>Enter your username or email address and we will send you a link to reset your password.</small></p>
												</form>
	                                        </div>

	                                        <div class="modal-footer">
	                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
	                                            <button type="button" class="btn btn-primary">Send reset link</button>
	                                        </div>
	                                    </div><!-- /.modal-content -->
	                                </div><!-- /.modal-dialog -->
	                            </div><!-- /.modal -->

								
							</div><!--/cols-->
						</div><!--/row-->

						<div class="signup tab-pane fade" id="signup">
							<div class="signup-brand">
								<img src="images/dummy/stilearn-logo2.png" alt="Sign up">
							</div>
							<h1 class="text-lead">Create an account</h1>
							<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Incidunt, ad, sint, ea, dicta dolor nesciunt adipisci molestias molestiae ex fugit sunt quia praesentium? Deserunt atque tenetur mollitia perspiciatis doloribus sint. By creating an account you agree to the <a href="#">Terms of Use</a> and <a href="#">Privacy Policy</a>.</p>
							<p>Already have an account, please <a data-toggle="tab" href="#signin">Signin</a>.</p>

							<form id="signup-form" data-validate="form" action="index.php" role="form">
								<div class="row">
									<div class="col-sm-5">
										<div class="form-group">
											<label class="control-label text-inverse" for="usernameUp">Username</label>
											<input type="text" class="form-control" name="usernameUp" id="usernameUp" required minlength="4" maxlength="12" autocomplete="off" />
											<p class="helper-block text-muted"><small>May contain letters, digits, dashes and underscores, and should be between 4 and 12 characters long.</small></p>
										</div>

										<div class="form-group">
											<label class="control-label text-inverse" for="emailUp">Email</label>
											<input type="email" class="form-control" name="emailUp" id="emailUp" required autocomplete="off" />
											<p class="helper-block text-muted"><small><strong>Type carefully!</strong> You will be sent a confirmation email.</small></p>
										</div>

										<div class="form-group">
											<label class="control-label text-inverse" for="passwordUp">Password</label>
											<input type="password" class="form-control" name="passwordUp" id="passwordUp" required minlength="4" />
											<p class="helper-block text-muted"><small>The longer the better. Include numbers for protein.</small></p>
										</div>

										<div class="form-group">
											<label class="control-label text-inverse" for="cpasswordUp">Confirm Password</label>
											<input type="password" class="form-control" name="cpasswordUp" id="cpasswordUp"  equalto="#passwordUp" />
											<p class="helper-block text-muted"><small>Enter your password again!</small></p>
										</div>

										<div class="form-group margin-top">
											<div class="nice-checkbox">
												<input class="checkbox-o" type="checkbox" name="newsletter" id="newsletter" checked />
												<label for="newsletter">Sign me up for the newsletter</label>
											</div>
										</div>

										<div class="form-group form-actions">
											<input type="submit" class="btn btn-primary" value="Create account">
										</div><!--/form-group-->

									</div><!--/cols-->
								</div><!--/row-->

							</form><!--/#signup-form-->
						</div><!--/#signup-->

					</div><!--/tab-content-->

					<div class="signin-footer">
						<ul class="list-inline pull-right">
							<li><a href="#">Knowledge base</a></li>
						</ul>
						<ul class="list-inline">
							<li>&copy; 2014 Stilearning</li>
							<li><a href="#">Terms of Use</a></li>
							<li><a href="#">Privacy Policy</a></li>
						</ul>
					</div>

				</div><!--/signin-wapper-->

			</div><!--/container-->
		</div><!--/content-->



        <!-- javascript
        ================================================== -->
        <!-- List of dependencies file, please check on readme.txt! (Purchase only) -->

        <!-- build:js scripts/vendor-main.js -->
        <!-- bower:js -->
        <script src="bower_components/jquery/jquery.js"></script>
        <script src="bower_components/jqueryui/ui/jquery-ui.js"></script>
        <script src="bower_components/jqueryui-touch-punch/jquery.ui.touch-punch.min.js"></script>
        <script src="bower_components/bootstrap/dist/js/bootstrap.js"></script>
        <!-- endbuild -->
        
        <!-- build:js scripts/vendor-usefull.js -->
        <script src="bower_components/pace/pace.min.js"></script>
        <script src="bower_components/jquery-pjax/jquery.pjax.js"></script>
        <script src="bower_components/masonry/masonry.pkgd.min.js"></script>
        <script src="bower_components/screenfull/dist/screenfull.min.js"></script>
        <script src="bower_components/jquery.nicescroll/jquery.nicescroll.min.js"></script>
        <script src="bower_components/countUp.js/countUp.min.js"></script>
        <script src="bower_components/skycons/skycons.js"></script>
        <script src="bower_components/jquery.lazyload/jquery.lazyload.min.js"></script>
        <script src="bower_components/WOW/dist/wow.min.js"></script>
        <!-- endbuild -->

        <!-- build:js scripts/vendor-form.js -->
        <script src="bower_components/jquery.validation/jquery.validate.js"></script>
        <script src="bower_components/jquery.validation/additional-methods.js"></script>
        <script src="bower_components/autogrow-textarea/jquery.autogrowtextarea.min.js"></script>
        <script src="bower_components/typeahead.js/dist/typeahead.min.js"></script>
        <script src="bower_components/jQuery-Mask-Plugin/jquery.mask.min.js"></script>
        <script src="bower_components/jquery.tagsinput/jquery.tagsinput.min.js"></script>
        <script src="bower_components/multiselect/js/jquery.multi-select.js"></script>
        <script src="bower_components/select2/select2.js"></script>
        <script src="bower_components/jquery-selectboxit/src/javascripts/jquery.selectBoxIt.js"></script>
        <script src="bower_components/momentjs/moment.js"></script>
        <script src="bower_components/bootstrap-daterangepicker/daterangepicker.js"></script>
        <script src="bower_components/bootstrap-datepicker/js/bootstrap-datepicker.js"></script>
        <script src="bower_components/bootstrap-timepicker/js/bootstrap-timepicker.js"></script>
        <script src="bower_components/jquery-minicolors/jquery.minicolors.min.js"></script>
        <script src="bower_components/dropzone/downloads/dropzone.min.js"></script>
        <script src="bower_components/jquery-steps/build/jquery.steps.min.js"></script>
        <script src="bower_components/fullcalendar/fullcalendar.js"></script>
        <!-- endbuild -->
        
        <!-- build:js scripts/vendor-editor.js -->
        <script src="bower_components/wysihtml5/dist/wysihtml5-0.3.0.js"></script>
        <script src="bower_components/bootstrap-wysihtml5/dist/bootstrap-wysihtml5-0.0.2.js"></script>
        <script src="bower_components/bootstrap-markdown/js/markdown.js"></script>
        <script src="bower_components/bootstrap-markdown/js/to-markdown.js"></script>
        <script src="bower_components/bootstrap-markdown/js/bootstrap-markdown.js"></script>
        <!-- endbuild -->
        
        
        <!-- build:js scripts/excanvas.js -->
        <!--[if lte IE 8]><script language="javascript" type="text/javascript" src="bower_components/flot/excanvas.min.js"></script><![endif]-->
        <!-- endbuild -->

        <!-- build:js scripts/vendor-graph.js -->
        <script src="bower_components/raphael/raphael-min.js"></script>
        <script src="bower_components/morris.js/morris.min.js"></script>
        <script src="bower_components/flot/jquery.flot.js"></script>
        <script src="bower_components/flot/jquery.flot.resize.js"></script>
        <script src="bower_components/flot/jquery.flot.categories.js"></script>
        <script src="bower_components/flot/jquery.flot.time.js"></script>
        <script src="bower_components/flot-axislabels/jquery.flot.axislabels.js"></script>
        <script src="bower_components/jquery.easy-pie-chart/dist/jquery.easypiechart.js"></script>
        <script src="bower_components/sparkline/dist/jquery.sparkline.min.js"></script>
        <!-- endbuild -->
    
        <!-- build:js scripts/vendor-table.js -->
        <script src="bower_components/datatables/media/js/jquery.dataTables.js"></script>
        <script src="bower_components/datatables-tools/js/dataTables.tableTools.js"></script>
        <script src="bower_components/datatables-bootstrap3/BS3/assets/js/datatables.js"></script>
        <script src="bower_components/jquery.tablesorter/js/jquery.tablesorter.js"></script>
        <script src="bower_components/jquery.tablesorter/js/jquery.tablesorter.widgets.js"></script>
        <script src="bower_components/jquery.tablesorter/addons/pager/jquery.tablesorter.pager.js"></script>
        <!-- endbuild -->

        <!-- build:js scripts/vendor-maps.js -->
        <script src="bower_components/jqvmap/jqvmap/jquery.vmap.min.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/jquery.vmap.world.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/jquery.vmap.algeria.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/jquery.vmap.france.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/jquery.vmap.germany.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/jquery.vmap.russia.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/jquery.vmap.usa.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/continents/jquery.vmap.africa.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/continents/jquery.vmap.asia.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/continents/jquery.vmap.australia.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/continents/jquery.vmap.europe.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/continents/jquery.vmap.north-america.js"></script>
        <script src="bower_components/jqvmap/jqvmap/maps/continents/jquery.vmap.south-america.js"></script>
        <script src="bower_components/jqvmap/jqvmap/data/jquery.vmap.sampledata.js"></script>
        <!-- endbuild -->
        
        <!-- build:js scripts/vendor-util.js -->
        <script src="bower_components/holderjs/holder.js"></script>
        <!-- endbower -->
        <!-- endbuild -->


        <!-- required stilearn template js -->
        <!-- build:js scripts/main.js -->
        <script src="scripts/bootstrap-jasny/js/fileinput.js"></script>
        <script src="scripts/js-prototype.js"></script>
        <script src="scripts/slip.js"></script>
        <script src="scripts/hogan-2.0.0.js"></script>        
        <script src="scripts/theme-setup.js"></script>
        <script src="scripts/chat-setup.js"></script>
        <script src="scripts/panel-setup.js"></script>
        <!-- endbuild -->

        <!-- This scripts will be reload after pjax or if popstate event is active (use with class .re-execute) -->
        <!-- build:js scripts/initializer.js -->
        <script class="re-execute" src="scripts/google-code-prettify/run_prettify.js"></script>
        <script class="re-execute" src="scripts/bootstrap-setup.js"></script>
        <script class="re-execute" src="scripts/jqueryui-setup.js"></script>
        <script class="re-execute" src="scripts/dependencies-setup.js"></script>
        <script class="re-execute" src="scripts/demo-setup.js"></script>
        <!-- endbuild -->

    </body>
</html>
