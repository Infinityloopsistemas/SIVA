<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- MORRIS CHART
                    ================================================== -->
                    <!-- Morris.js  -->
                    <div id="panel-morris" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button data-refresh="#panel-morris" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-morris" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-morris" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-morris" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Morris.js</h3>
                        </div><!-- /panel-heading -->
                        
                        <div class="panel-body">
                            <p>Start by adding a <code>&lt;div&gt;</code> to your page that will contain your chart. Make sure it has an ID so you can refer to it in your Javascript later.</p>
                            <pre class="prettyprint">&lt;div id=&quot;mymorrischart&quot; style=&quot;height: 250px;&quot;&gt;&lt;/div&gt;</pre>
                            <p><strong>NOTE: </strong> <em>in order to display something, you’ll need to have given the div some dimensions. Here I’ve used inline CSS just for illustration.</em></p>
                        </div><!-- /panel-body -->
                        <div class="table-responsive">
                            <table class="table table-bordered">
                                <tbody>
                                    <tr>
                                        <td class="demo-graph">
                                            <div class="demo-graph-caption">Jaguar 'E' Type vehicles in the UK</div>
                                            <div id="morris-graph"></div>
                                        </td>
                                        <td class="demo-graph">
                                            <div class="demo-graph-caption">iPhone Vs Android</div>
                                            <div id="morris-bar"></div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="demo-graph">
                                            <div class="demo-graph-caption">Quarterly Apple iOS device unit sales</div>
                                            <div id="morris-area"></div>
                                        </td>
                                        <td class="demo-graph">
                                            <div class="demo-graph-caption">Donut flavours</div>
                                            <div id="morris-donut"></div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table><!--/table-->
                        </div><!--/table-responsive-->
                    </div><!--/panel-morris-->