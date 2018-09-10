<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- COLLAPSE
                    ================================================== -->
					<div class="panel-group" id="accordion1">
						<div class="panel panel-default">
							<div class="panel-heading">
								<h4 class="panel-title">
									<a data-toggle="collapse" data-parent="#accordion1" href="#collapseOne">
										Collapsible Group Item #1
									</a>
								</h4><!-- /panel-title -->
							</div><!-- /panel-heading -->
							<div id="collapseOne" class="panel-collapse collapse in">
								<div class="panel-body">
									<p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable <VHS class="p"></p></VHS>
								</div><!-- /panel-body -->
							</div><!-- /panel-collapse -->
						</div><!-- /panel -->

						<div class="panel panel-default">
							<div class="panel-heading">
								<h4 class="panel-title">
									<a data-toggle="collapse" data-parent="#accordion1" href="#collapseTwo">
										Collapsible Group Item #2
									</a>
								</h4><!-- /panel-title-->
							</div><!-- /panel-heading-->
							<div id="collapseTwo" class="panel-collapse collapse">
								<div class="panel-body">
									<p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</p>
								</div><!-- /panel-body-->
							</div><!-- /panel-collapse-->
						</div><!-- /panel-->

						<div class="panel panel-default">
							<div class="panel-heading">
								<h4 class="panel-title">
									<a data-toggle="collapse" data-parent="#accordion1" href="#collapseThree">
										Collapsible Group Item #3
									</a>
								</h4><!-- /panel-title-->
							</div><!-- /panel-heading-->
							<div id="collapseThree" class="panel-collapse collapse">
								<div class="panel-body">
									<p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</p>
								</div><!-- /panel-body-->
							</div><!-- /panel-collapse-->
						</div><!-- /panel-->
					</div><!-- /panel-group -->




					<div class="row">
						<div class="col-md-6">
							<div class="panel-group" id="accordion2">
								<div id="collapse-panact" class="panel panel-default">
									<div class="panel-heading">
										<div class="panel-actions">
											<button data-refresh="#collapse-panact" data-loader="loader-cloud" title="refresh" class="btn-panel">
	                                            <i class="fa fa-refresh"></i>
	                                        </button>
											<a data-toggle="collapse" data-parent="#accordion2" href="#collapseOne2" class="btn-panel btn-collapse">
												<i class="fa fa-angle-down"></i>
											</a>
	                                        <button data-close="#collapse-panact" title="close" data-animate="flipOutX" class="btn-panel">
	                                            <i class="fa fa-times"></i>
	                                        </button>
										</div><!-- /panel-actions -->
										<h4 class="panel-title">
											<a data-toggle="collapse" data-parent="#accordion2" href="#collapseOne2">
												With Panel Actions
											</a>
										</h4><!-- /panel-title-->
									</div><!-- /panel-heading-->
									<div id="collapseOne2" class="panel-collapse collapse in">
										<div class="panel-body">
											<p>You can add All of Panel Actions Features on Collapsible group, <em>except</em> <code>expand</code> <em>feature</em>. Please see the <a data-pjax=".content-body" href="widget-panel.php">Widget Panel</a> demo.</p>
										</div><!-- /panel-body-->
									</div><!-- /panel-collapse-->
								</div><!-- /panel-->

								<div class="panel panel-default">
									<div class="panel-heading">
										<div class="panel-actions">
											<div class="btn-group">
	                                            <button title="Chose a color" class="btn-panel disable-tooltip dropdown-toggle" data-toggle="dropdown">
	                                                <i class="fa fa-tint"></i>
	                                            </button>
	                                            <ul class="dropdown-menu dropdown-inline bg-midnight pull-right" role="menu">
	                                                <li>
	                                                    <a rel="tooltip" title="Default" data-context="panel-default" data-target="#accordion2 .panel" class="color-pick bg-cloud"></a>
	                                                </li>
	                                                <li>
	                                                    <a rel="tooltip" title="Primary" data-context="panel-primary" data-target="#accordion2 .panel" class="color-pick bg-primary"></a>
	                                                </li>
	                                                <li>
	                                                    <a rel="tooltip" title="Success" data-context="panel-success" data-target="#accordion2 .panel" class="color-pick bg-success"></a>
	                                                </li>
	                                                <li>
	                                                    <a rel="tooltip" title="Info" data-context="panel-info" data-target="#accordion2 .panel" class="color-pick bg-info"></a>
	                                                </li>
	                                                <li>
	                                                    <a rel="tooltip" title="Warning" data-context="panel-warning" data-target="#accordion2 .panel" class="color-pick bg-warning"></a>
	                                                </li>
	                                                <li>
	                                                    <a rel="tooltip" title="Danger" data-context="panel-danger" data-target="#accordion2 .panel" class="color-pick bg-danger"></a>
	                                                </li>
	                                            </ul>
	                                        </div>
											<a data-toggle="collapse" data-parent="#accordion2" href="#collapseTwo2" class="btn-panel btn-collapse btn-collapsed">
												<i class="fa fa-angle-down"></i>
											</a>
										</div><!-- /panel-actions -->
										<h4 class="panel-title">
											<a data-toggle="collapse" data-parent="#accordion2" href="#collapseTwo2">
												Contextual
											</a>
										</h4><!-- /panel-title -->
									</div><!-- /panel-heading -->
									<div id="collapseTwo2" class="panel-collapse collapse">
										<div class="panel-body">
											<p>Easily make a panel more meaningful to a particular context by adding any of the contextual state classes (panel-primary, panel-success, panel-info, panel-warning, panel-danger).</p>
										</div><!-- /panel-body -->
									</div><!-- /panel-collapse -->
								</div><!-- /panel -->

								<div class="panel panel-default">
									<div class="panel-heading">
										<div class="panel-actions">
											<a data-toggle="collapse" data-parent="#accordion2" href="#collapseThree2" class="btn-panel btn-collapse btn-collapsed">
												<i class="fa fa-angle-down"></i>
											</a>
										</div><!-- /panel-actions -->
										<h4 class="panel-title">
											<a data-toggle="collapse" data-parent="#accordion2" href="#collapseThree2">
												Buttons collapse
											</a>
										</h4><!-- /panel-title-->
									</div><!-- /panel-heading-->
									<div id="collapseThree2" class="panel-collapse collapse">
										<div class="panel-body">
											<p>Its a different way to collapse panel inside collapsible group. You must define <code>data-toggle="collapse"</code> as a custom actions for collapse the panel. Don't forget to define target panel with <code>data-target</code> and target panel collapse with <code>href</code>.</p>
											<p><strong>Note:</strong> required class <code>.btn-collapse</code> and <code>.btn-collapsed</code>. Refer to the demo to see this in action.</p>
										</div><!-- /panel-body-->
									</div><!-- /panel-collapse-->
								</div><!-- /panel-->
							</div><!-- /panel-group -->
						</div><!-- /cols -->



						<div class="col-md-6">
							<div class="panel-group" id="accordion3" data-toggle="sortable-widget" data-containment="#accordion3">
								<div class="panel panel-primary border-inverse sortable-widget-item">
									<div class="panel-heading bg-inverse">
										<div class="panel-actions">
											<a data-toggle="collapse" data-parent="#accordion3" href="#collapseOne3" class="btn-panel btn-collapse">
												<i class="fa fa-angle-down"></i>
											</a>
										</div><!-- /panel-actions -->
										<h4 class="panel-title sortable-widget-handle">
											<a data-toggle="collapse" data-parent="#accordion3" href="#collapseOne3">
												Inverse style
											</a>
										</h4><!-- /panel-title-->
									</div><!-- /panel-heading-->
									<div id="collapseOne3" class="panel-collapse collapse in">
										<div class="panel-body bg-inverse border-inverse">
											<p>Customize panel with <a data-pjax=".content-body" href="helper-classes.php">Helper Classes</a>. Just play and get your style <i class="fa fa-smile-o"></i>. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe, aliquam, odit explicabo voluptatem optio debitis excepturi minus quis quae quaerat! Aliquam, magni nulla aperiam expedita aliquid reprehenderit dignissimos quis architecto.</p>
										</div><!-- /panel-body-->
									</div><!-- /panel-collapse-->
								</div><!-- /panel-->

								<div class="panel panel-primary border-inverse sortable-widget-item">
									<div class="panel-heading bg-inverse">
										<div class="panel-actions">
											<a data-toggle="collapse" data-parent="#accordion3" href="#collapseTwo3" class="btn-panel btn-collapse btn-collapsed">
												<i class="fa fa-angle-down"></i>
											</a>
										</div><!-- /panel-actions -->
										<h4 class="panel-title sortable-widget-handle">
											<a data-toggle="collapse" data-parent="#accordion3" href="#collapseTwo3">
												Play with Helper Classes
											</a>
										</h4><!-- /panel-title -->
									</div><!-- /panel-heading -->
									<div id="collapseTwo3" class="panel-collapse collapse">
										<div class="panel-body bg-inverse border-inverse">
											<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore, blanditiis nisi sed modi quae maxime fuga magnam quidem. Repellat, consequatur aut officia assumenda labore non incidunt inventore quasi doloribus magnam!</p>
										</div><!-- /panel-body -->
									</div><!-- /panel-collapse -->
								</div><!-- /panel -->

								<div class="panel panel-primary border-inverse sortable-widget-item">
									<div class="panel-heading bg-inverse">
										<div class="panel-actions">
											<a data-toggle="collapse" data-parent="#accordion3" href="#collapseThree3" class="btn-panel btn-collapse btn-collapsed">
												<i class="fa fa-angle-down"></i>
											</a>
										</div><!-- /panel-actions -->
										<h4 class="panel-title sortable-widget-handle">
											<a data-toggle="collapse" data-parent="#accordion3" href="#collapseThree3">
												Enjoy It!
											</a>
										</h4><!-- /panel-title-->
									</div><!-- /panel-heading-->
									<div id="collapseThree3" class="panel-collapse collapse">
										<div class="panel-body bg-inverse border-inverse">
											<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut, cum, unde, laborum, dicta obcaecati quo ratione sapiente quasi temporibus ea similique sunt tenetur suscipit perspiciatis nulla nostrum eum velit tempora!</p>
										</div><!-- /panel-body-->
									</div><!-- /panel-collapse-->
								</div><!-- /panel-->
							</div><!-- /panel-group -->
						</div><!-- /cols -->
					</div><!-- /row -->