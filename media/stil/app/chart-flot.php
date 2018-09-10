<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- FLOT CHART
                    ================================================== -->
                    <!-- Flotchart  -->
                    <div id="panel-flotchart" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button data-refresh="#panel-flotchart" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-flotchart" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-flotchart" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-flotchart" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Flot Chart</h3>
                        </div><!-- /panel-heading -->
                        
                        <div class="panel-body">
                            <p class="lead">Attractive JavaScript plotting for jQuery</p>
                            <p>Flot is a pure JavaScript plotting library for jQuery, with a focus on simple usage, attractive looks and interactive features.</p>
                            <p><strong>NOTE: </strong> We didn't include support for flot pie. Alternativally, you can use <a rel="tooltip" title="Morris.js" data-pjax=".content-body" href="chart-morris.php">Morris Donut</a> or <a rel="tooltip" title="Easy Pie Chart" data-pjax=".content-body" href="chart-inline.php">Easy Pie Chart</a>.</p>
                        </div><!-- /panel-body -->
                        <div class="table-responsive">
                            <table class="table table-bordered">
                                <tbody>
                                    <tr>
                                        <td colspan="2" class="demo-flot">
                                            <div class="demo-flot-caption">Combine Chart</div>
                                            <div id="flot-combine" class="graph"></div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="demo-flot">
                                            <div class="demo-flot-caption">Line Chart</div>
                                            <div id="flot-line" class="graph"></div>
                                        </td>
                                        <td class="demo-flot">
                                            <div class="demo-flot-caption">Bar Chart</div>
                                            <div id="flot-bar" class="graph"></div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="demo-flot">
                                            <div class="demo-flot-caption">Area Chart</div>
                                            <div id="flot-area" class="graph"></div>
                                        </td>
                                        <td class="demo-flot">
                                            <div class="demo-flot-caption">Horizontal Bar Chart</div>
                                            <div id="flot-barhor" class="graph"></div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="demo-flot">
                                            <div class="demo-flot-caption">Realtime Chart</div>
                                            <div id="flot-realtime" class="graph"></div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table><!--/table-->
                        </div><!--/table-responsive-->
                    </div><!--/panel-flotchart-->