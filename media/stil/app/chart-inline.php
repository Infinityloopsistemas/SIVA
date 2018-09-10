<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- INLINE CHART
                    ================================================== -->
                    <!-- Easy Pie Chart  -->
                    <div id="panel-easypie" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button id="updatePieCharts" title="refresh chart" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-easypie" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-easypie" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-easypie" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Easy Pie Chart</h3>
                        </div><!-- /panel-heading -->
                        
                        <div class="panel-body bordered-bottom">
                            <div class="text-center">
                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="20" data-barColor="#13A89E">
                                        <span>20%</span>
                                    </div>
                                    <div class="easyPieChart-label">New visits</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="40" data-barColor="#5BB75B">
                                        <span>40%</span>
                                    </div>
                                    <div class="easyPieChart-label">Bounce rate</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="60" data-barColor="#FAA732">
                                        <span>60%</span>
                                    </div>
                                    <div class="easyPieChart-label">Server load</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="80" data-barColor="#DA4F49">
                                        <span>80%</span>
                                    </div>
                                    <div class="easyPieChart-label">Disk space</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="90" data-barColor="#49AFCD">
                                        <span>100%</span>
                                    </div>
                                    <div class="easyPieChart-label">Bandwidth</div>
                                </div><!-- /easy-pie-chart -->
                            </div><!-- /center-align -->
                        </div><!-- /panel-body -->

                        <div class="panel-body bordered-bottom">
                            <p class="text-muted"><strong>Track and scale color</strong></p>
                            <div class="text-center">
                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="20" data-scaleColor="#13A89E">
                                        <span>20%</span>
                                    </div>
                                    <div class="easyPieChart-label">New visits</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="40" data-trackColor="#394264" data-scaleColor="#394264">
                                        <span>40%</span>
                                    </div>
                                    <div class="easyPieChart-label">Bounce rate</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="60" data-trackColor="false" data-scaleColor="#DA4F49">
                                        <span>60%</span>
                                    </div>
                                    <div class="easyPieChart-label">Server load</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="80" data-trackColor="false" data-scaleColor="false">
                                        <span>80%</span>
                                    </div>
                                    <div class="easyPieChart-label">Disk space</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="90" data-barColor="#394264" data-trackColor="#DA4F49" data-scaleColor='false'>
                                        <span>100%</span>
                                    </div>
                                    <div class="easyPieChart-label">Bandwidth</div>
                                </div><!-- /easy-pie-chart -->
                            </div><!-- /center-align -->
                        </div><!-- /panel-body -->

                        <div class="panel-body bordered-bottom">
                            <p class="text-muted"><strong>Sizing and rotate</strong></p>
                            <div class="text-center">
                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="20" data-size="90">
                                        <span>20%</span>
                                    </div>
                                    <div class="easyPieChart-label">Size 80</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="40" data-barColor="#394264" data-size="160" data-lineWidth="8">
                                        <span class="text-lg">40%</span>
                                    </div>
                                    <div class="easyPieChart-label">lineWidth 8</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="60" data-rotate="90">
                                        <span>60%</span>
                                    </div>
                                    <div class="easyPieChart-label">Rotate 90</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="80" data-barColor="#394264" data-size="200" data-lineWidth="10" data-rotate="180">
                                        <span class="text-xg">80%</span>
                                    </div>
                                    <div class="easyPieChart-label">Combine large</div>
                                </div><!-- /easy-pie-chart -->

                                <div class="easy-pie-chart">
                                    <div class="easyPieChart" data-percent="90" data-size="70" data-lineWidth="3" data-rotate="270">
                                        <span>100%</span>
                                    </div>
                                    <div class="easyPieChart-label">Combine small</div>
                                </div><!-- /easy-pie-chart -->
                            </div><!-- /center-align -->
                        </div><!-- /panel-body -->

                        <div class="panel-body">
                            <p><strong>NOTE: </strong> Please Click Panel Refresh <code><small><i class="fa fa-refresh"></i></small></code> to update demo chart.</p>
                            <p>Just play with data attribute to make easyPieChart as you want:</p>
                            <pre class="prettyprint no-padding">&lt;div class="easyPieChart" 
    data-barColor="#13A89E" 
    data-trackColor="#ecf0f1" 
    data-scaleColor="#bdc3c7" 
    data-percent="90" 
    data-size="160" 
    data-lineWidth="10" 
    data-rotate="270"
&gt;&lt;/div&gt;</pre>
                        </div><!-- /panel-body -->
                    </div><!--/panel-easypie-->






                    <!-- Sparkline -->
                    <div id="panel-sparkline" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-icon"><i class="icon ion-ios7-pie-outline"></i></div>
                            <div class="panel-actions">
                                <button data-refresh="#panel-sparkline" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-sparkline" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-sparkline" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-sparkline" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Sparklines</h3>
                        </div><!-- /panel-heading -->
                        <div class="panel-body">
                            <div class="callout callout-warning">
                                <h4>Project Page</h4>
                                <p>See the <a target="_blank" href="http://omnipotent.net/jquery.sparkline/">jQuery Sparkline project page</a> for live examples and documentation.</p>
                            </div>
                            <div class="row">
                                <div class="col-md-6">
                                    <p>
                                        Mouse speed <span id="mousespeed">Loading..</span>
                                    </p>
                                    <p>
                                        Inline <span class="sparkline">10,8,9,3,5,8,5</span> 
                                        line graphs 
                                        <span class="sparkline">8,4,0,0,0,0,1,4,4,10,10,10,10,0,0,0,4,6,5,9,10</span>
                                    </p>

                                    <p>
                                        Bar charts <span class="sparkbar">10,8,9,3,5,8,5</span> 
                                        negative values: <span class="sparkbar">-3,1,2,0,3,-1</span>
                                        stacked: <span class="sparkbar">0:2,2:4,4:2,4:1</span>
                                    </p>

                                    <p>
                                        Composite inline 
                                        <span id="compositeline">8,4,0,0,0,0,1,4,4,10,10,10,10,0,0,0,4,6,5,9,10</span>
                                    </p>
                                    <p>
                                        Inline with normal range 
                                        <span id="normalline">8,4,0,0,0,0,1,4,4,10,10,10,10,0,0,0,4,6,5,9,10</span>
                                    </p>
                                    <p>
                                        Composite bar 
                                        <span id="compositebar">4,6,7,7,4,3,2,1,4</span>
                                    </p>
                                    <p>
                                        Discrete 
                                        <span class="discrete1">4,6,7,7,4,3,2,1,4,4,5,6,7,6,6,2,4,5</span><br />

                                        Discrete with threshold 
                                        <span id="discrete2">4,6,7,7,4,3,2,1,4</span>
                                    </p>
                                    <p>
                                        Customize size and colours 
                                        <span id="linecustom">10,8,9,3,5,8,5,7</span>
                                    </p>
                                </div><!-- /cols -->
                                <div class="col-md-6">
                                    <p>
                                        Tristate charts 
                                        <span class="sparktristate">1,1,0,1,-1,-1,1,-1,0,0,1,1</span><br />
                                        (think games won, lost or drawn)
                                    </p>
                                    <p>
                                        Tristate chart using a colour map: 
                                        <span class="sparktristatecols">1,2,0,2,-1,-2,1,-2,0,0,1,1</span>
                                    </p>
                                    <p>
                                        Box Plot: <span class="sparkboxplot">4,27,34,52,54,59,61,68,78,82,85,87,91,93,100</span><br />
                                        Pre-computed box plot <span class="sparkboxplotraw">Loading..</span>
                                    </p>
                                    <p>
                                        Pie charts 
                                        <span class="sparkpie">1,1,2</span> 
                                        <span class="sparkpie">1,5</span> 
                                        <span class="sparkpie">20,50,80</span>
                                    </p>
                                    <p>
                                        Bullet charts<br />
                                        <span class="sparkbullet">10,12,12,9,7</span><br />
                                        <span class="sparkbullet">14,12,12,9,7</span><br />
                                        <span class="sparkbullet">10,12,14,9,7</span><br />
                                    </p>
                                </div><!-- /cols -->
                            </div><!-- /row -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-sparkline -->