<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- LOADERS
                    ================================================== -->
                    <div id="panel-loaders" class="panel panel-default">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button data-refresh="#panel-loaders" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-loaders" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-loaders" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title"><i class="fa fa-spin fa-spinner"></i> Loaders Kit</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <div class="row">
                            	<div class="col-md-3">
                            		<p><code>.loader-timer</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-timer"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-typing</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-typing"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-location-indicator</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-location-indicator"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-dashboard</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-dashboard"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-battery</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-battery"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-magnifier</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-magnifier"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-help</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-help"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-eye</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-eye"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-coffee-cup</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-coffee-cup"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-square</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-square"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-circle</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-circle"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-cloud</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-cloud"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-spinner</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-spinner"></div>
                            		</div>
                            	</div><!--/cols-->
                            </div><!--/row-->

                            <h4>Contextual alternatives</h4>
                            <p>Like other components, easily make a Loaders more meaningful to a particular context by adding any of the contextual state classes (primary, success, info, warning, danger) <code>.loadername-contextname</code>. Refer to the demo to see this in action.</p><br>
                            
                            <div class="row">
                            	<div class="col-md-3">
                            		<p><code>.loader-timer.loader-time-primary</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-timer loader-timer-primary"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-typing.loader-typing-success</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-typing loader-typing-success"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-square.loader-square-info</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-square loader-square-info"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-battery.loader-battery-warning</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-battery loader-battery-warning"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-eye.loader-eye-danger</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-eye loader-eye-danger"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-circle.loader-circle-primary</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-circle loader-circle-primary"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-spinner.loader-spinner-success</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-spinner loader-spinner-success"></div>
                            		</div>
                            	</div><!--/cols-->

                            	<div class="col-md-3">
                            		<p><code>.loader-cloud.loader-cloud-info</code></p>
                            		<div class="demo-box-loader">
                            			<div class="loader-cloud loader-cloud-info"></div>
                            		</div>
                            	</div><!--/cols-->
                        	</div><!--/row-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-loaders -->