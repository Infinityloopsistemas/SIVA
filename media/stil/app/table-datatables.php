<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- DATATABLES
                    ================================================== -->
                    <div class="callout callout-info">
                    	<h4>Initialize</h4>
                    	<p>Activate Datatables with <code>.datatables</code> for simple Datatables and <code>.datatables-tools</code> if you want enable TableTools feature. Use with external data with <code>data-source="url"</code> (Refer to the demo to see this in action).</p>
                    	<p>Datatables come with optionals pagination <code>data-page="value"</code>.</p>
                    	<p><strong>NOTE: </strong> Posible value for pagination <code>bs_normal</code>, <code>bs_two_button</code>, <code>bs_four_button</code>, <code>bs_full</code> (default).</p>
                    </div>
                    <!-- Datatables Bootstrap3 -->
                    <div id="panel-datatables" class="panel panel-default">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button data-refresh="#panel-datatables" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-datatables" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-datatables" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-datatables" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Datatables</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
		                    <div class="table-responsive table-responsive-datatables">
		                    	<table data-source="data-sample/datatables.json" data-page="bs_four_button" class="datatable table table-hover table-bordered">
									<thead>
										<tr>
											<th>Rendering engine</th>
											<th>Browser</th>
											<th>Platform(s)</th>
											<th>Engine version</th>
											<th>CSS grade</th>
										</tr>
									</thead><!--/thead-->

									<tbody></tbody><!--/tbody-->
									
									<tfoot>
										<tr>
											<th>Rendering engine</th>
											<th>Browser</th>
											<th>Platform(s)</th>
											<th>Engine version</th>
											<th>CSS grade</th>
										</tr>
									</tfoot><!--/tfoot-->
								</table><!--/table tools-->
		                    </div><!--/table-responsive-->
						</div><!--/panel-body-->
					</div><!--/panel-datatables-->




					<!-- DatatableTools -->
					<div id="panel-datatablestools" class="panel panel-default">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button data-refresh="#panel-datatablestools" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-datatablestools" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-datatablestools" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-datatablestools" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Datatables Tools</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
		                    <div class="table-responsive table-responsive-datatables">
		                    	<table data-source="data-sample/datatables2.json" class="datatable-tools table table-striped table-bordered">
									<thead>
										<tr>
											<th>#</th>
											<th>Name</th>
											<th>Company</th>
											<th>Region</th>
											<th>Country</th>
										</tr>
									</thead><!--/thead-->

									<tbody></tbody><!--/tbody-->
									
									<tfoot>
										<tr>
											<th>#</th>
											<th>Name</th>
											<th>Company</th>
											<th>Region</th>
											<th>Country</th>
										</tr>
									</tfoot><!--/tfoot-->
								</table><!--/table tools-->
		                    </div><!--/table-responsive-->
						</div><!--/panel-body-->
					</div><!--/panel-datatablestools-->