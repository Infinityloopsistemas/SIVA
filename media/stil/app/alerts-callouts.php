<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- ALERT AND CALLOUT
                    ================================================== -->
                    <div class="row">
                        <div class="col-md-12" data-toggle="sortable-widget">
                            <!-- ALERT AND CALLOUT  -->
                            <div id="panel-alco" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-alco" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-alco" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-alco" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-alco" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Alerts & Callouts</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bordered-bottom">
                                    <p>Provide contextual feedback messages for typical user actions with the handful of available and flexible alert messages. No default class, you're required to specify a type via contextual class. Choose from <code>success, info, warning, or danger</code>.</p>
                                    <div class="callout">
                                        <h4>Ensure proper behavior across all devices</h4>
                                        <p>Be sure to use the <code>&lt;button&gt;</code> element with the <code>data-dismiss=&quot;alert&quot;</code> data attribute.</p>
                                    </div>
                                    <div>
                                        <div class="alert alert-success fade in">
                                            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                            <strong>Well done!</strong> You successfully read this important alert message.
                                        </div>
                                        <div class="alert alert-info fade in">
                                            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                            <strong>Heads up!</strong> This alert needs your attention, but it's not super important.
                                        </div>
                                        <div class="alert alert-warning fade in">
                                            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                            <strong>Warning!</strong> Best check yo self, you're not looking too good.
                                        </div>
                                        <div class="alert alert-danger fade in">
                                            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                            <strong>Oh snap!</strong> Change a few things up and try submitting again.
                                        </div>
                                    </div>
                                    <pre class="no-padding prettyprint">&lt;div class=&quot;alert alert-success&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;alert alert-info&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;alert alert-warning&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;alert alert-danger&quot;&gt;...&lt;/div&gt;</pre>
                                    
                                    <h4>Callout</h4>
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Context</strong></p>
                                            <div>
                                                <div class="callout callout-success fade in">
                                                    <h4>Well done!</h4>
                                                    <p>You successfully read this important message. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus, dolorum fugit voluptatem odio aut tempore.</p>
                                                </div>
                                                <div class="callout callout-info fade in">
                                                    <h4>Heads up!</h4>
                                                    <p>This message needs your attention, but it's not super important. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat, libero facere suscipit sapiente ut provident!</p>
                                                </div>
                                                <div class="callout callout-warning fade in">
                                                    <h4>Warning!</h4>
                                                    <p>Best check yo self, you're not looking too good. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero non quos explicabo facilis beatae laborum.</p>
                                                </div>
                                                <div class="callout callout-danger fade in">
                                                    <h4>Oh snap!</h4>
                                                    <p>Change a few things up and try submitting again. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deleniti ratione nisi quo consequuntur error quasi!</p>
                                                </div>
                                            </div>
                                        </div><!--/cols-->
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Right-aligned callout</strong> <code>.callout-right</code></p>
                                            <div>
                                                <div class="callout callout-success callout-right fade in">
                                                    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                                    <h4>Well done!</h4>
                                                    <p>You successfully read this important message. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem voluptatibus quis harum accusantium et quidem.</p>
                                                </div>
                                                <div class="callout callout-info callout-right fade in">
                                                    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                                    <h4>Heads up!</h4>
                                                    <p>This message needs your attention, but it's not super important. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Debitis, natus tempora libero maiores aliquam incidunt.</p>
                                                </div>
                                                <div class="callout callout-warning callout-right fade in">
                                                    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                                    <h4>Warning!</h4>
                                                    <p>Best check yo self, you're not looking too good. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Provident, commodi accusamus aliquam quas quis eos!</p>
                                                </div>
                                                <div class="callout callout-danger callout-right fade in">
                                                    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                                    <h4>Oh snap!</h4>
                                                    <p>Change a few things up and try submitting again. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate, quo nulla dicta dolor pariatur atque.</p>
                                                </div>
                                            </div>
                                        </div><!--/cols-->
                                    </div><!--/row-->
                                    <pre class="no-padding prettyprint">&lt;div class=&quot;callout callout-success&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;callout callout-info&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;callout callout-warning&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;callout callout-danger&quot;&gt;...&lt;/div&gt;</pre>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-alco -->
                        </div><!--/cols -->
                    </div><!--/row -->