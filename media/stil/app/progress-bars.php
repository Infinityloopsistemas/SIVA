<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- PROGRESSBAR
                    ================================================== -->
                    <div class="row">
                        <div class="col-md-12" data-toggle="sortable-widget">
                            <!-- PROGRESSBAR  -->
                            <div id="panel-progressbar" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-progressbar" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-progressbar" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-progressbar" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-progressbar" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Progress Bars</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bordered-bottom">
                                    <div class="callout callout-danger">
                                        <h4>Cross-browser compatibility</h4>
                                        <p>Progress bars use CSS3 transitions and animations to achieve some of their effects. These features are not supported in Internet Explorer 9 and below or older versions of Firefox. Opera 12 does not support animations.</p>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Contextual alternatives</strong></p>
                                            <div class="progress">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 75%">
                                                    <span class="sr-only">75% Complete</span>
                                                </div>
                                            </div>
                                            <div class="progress">
                                                <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 40%">
                                                    <span class="sr-only">40% Complete (success)</span>
                                                </div>
                                            </div>
                                            <div class="progress">
                                                <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%">
                                                    <span class="sr-only">20% Complete (info)</span>
                                                </div>
                                            </div>
                                            <div class="progress">
                                                <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                                    <span class="sr-only">60% Complete (warning)</span>
                                                </div>
                                            </div>
                                            <div class="progress">
                                                <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 80%">
                                                    <span class="sr-only">80% Complete (danger)</span>
                                                </div>
                                            </div>
                                            <div class="progress">
                                                <div class="progress-bar progress-bar-inverse" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100" style="width: 90%">
                                                    <span class="sr-only">90% Complete (inverse)</span>
                                                </div>
                                            </div>
                                        </div><!--/cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Inverse</strong></p>
                                            <div class="progress progress-inverse">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 75%">
                                                    <span class="sr-only">75% Complete</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-inverse-success">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 40%">
                                                    <span class="sr-only">40% Complete (success)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-inverse-info">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%">
                                                    <span class="sr-only">20% Complete (info)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-inverse-warning">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                                    <span class="sr-only">60% Complete (warning)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-inverse-danger">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 80%">
                                                    <span class="sr-only">80% Complete (danger)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-inverse-inverse">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100" style="width: 90%">
                                                    <span class="sr-only">90% Complete (inverse)</span>
                                                </div>
                                            </div>
                                        </div><!--/cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Flat</strong></p>
                                            <div class="progress progress-flat">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 75%">
                                                    <span class="sr-only">75% Complete</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-flat">
                                                <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 40%">
                                                    <span class="sr-only">40% Complete (success)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-flat">
                                                <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%">
                                                    <span class="sr-only">20% Complete (info)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-flat">
                                                <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                                    <span class="sr-only">60% Complete (warning)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-flat">
                                                <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 80%">
                                                    <span class="sr-only">80% Complete (danger)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-flat">
                                                <div class="progress-bar progress-bar-inverse" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100" style="width: 90%">
                                                    <span class="sr-only">90% Complete (inverse)</span>
                                                </div>
                                            </div>
                                        </div><!--/cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Striped</strong></p>
                                            <div class="progress progress-striped">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 75%">
                                                    <span class="sr-only">75% Complete</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-striped">
                                                <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 40%">
                                                    <span class="sr-only">40% Complete (success)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-striped">
                                                <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%">
                                                    <span class="sr-only">20% Complete (info)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-striped">
                                                <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                                    <span class="sr-only">60% Complete (warning)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-striped">
                                                <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 80%">
                                                    <span class="sr-only">80% Complete (danger)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-striped">
                                                <div class="progress-bar progress-bar-inverse" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100" style="width: 90%">
                                                    <span class="sr-only">90% Complete (inverse)</span>
                                                </div>
                                            </div>
                                        </div><!--/cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Animated</strong></p>
                                            <div class="progress progress-striped active">
                                                <div class="progress-bar"  role="progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100" style="width: 45%">
                                                    <span class="sr-only">45% Complete</span>
                                                </div>
                                            </div>
                                        </div><!--/cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Stacked</strong></p>
                                            <div class="progress progress-striped active">
                                                <div class="progress-bar" style="width: 35%">
                                                    <span class="sr-only">35% Complete (success)</span>
                                                </div>
                                                <div class="progress-bar progress-bar-success" style="width: 20%">
                                                    <span class="sr-only">20% Complete (success)</span>
                                                </div>
                                                <div class="progress-bar progress-bar-info" style="width: 10%">
                                                    <span class="sr-only">10% Complete (info)</span>
                                                </div>
                                            </div>
                                        </div><!--/cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Sizing</strong></p>
                                            <div class="progress progress-lg progress-striped">
                                                <div class="progress-bar" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 75%">
                                                    <span class="sr-only">75% Complete</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-striped">
                                                <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 40%">
                                                    <span class="sr-only">40% Complete (success)</span>
                                                </div>
                                            </div>
                                            <div class="progress progress-sm progress-striped">
                                                <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%">
                                                    <span class="sr-only">20% Complete</span>
                                                </div>
                                            </div>
                                        </div><!--/cols -->
                                    </div><!--/row -->

                                </div><!-- /panel-body -->
                            </div><!-- /panel-progressbar -->
                        </div><!--/cols -->
                    </div><!--/row -->