<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- MODAL
                    ================================================== -->
                    <div class="row">
                        <div class="col-md-12" data-toggle="sortable-widget">
                            <!-- MODAL -->
                            <div id="panel-modal" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-modal" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-modal" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-modal" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-modal" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Modal <small>Sound available</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>The modal plugin toggles your hidden content on demand, via data attributes or JavaScript. It also adds <code>.model-open</code> to the <code>&lt;body&gt;</code> to override default scrolling behavior and generates a <code>.modal-backdrop</code> to provide a click area for dismissing shown modals when clicking outside the modal.</p>
                                    <p>Activate a modal without writing JavaScript. Set <code>data-toggle="modal"</code> on a controller element, like a button, along with a <code>data-target="#foo"</code> or <code>href="#foo"</code> to target a specific modal to toggle.</p>
                                    <p>We add support for attribute <code>data-sound</code> to enable sound if Modal has been <code>shown</code>, also support custom value <code>data-sound=&quot;http://site.com/audio_name&quot;</code> without file extention (only support with <code>*.mp3</code> and <code>*.ogg</code>). To turn off sound feature just add <code>data-sound=&quot;off&quot;</code>. Available <code>data-sound</code> value:</p>
                                    <p><code>hello, bamboo, complete, note, pulse</code></p>
                                    <div class="callout callout-warning">
                                        <h4>Make modals accessible</h4>
                                        <p>Be sure to add <code>role="dialog"</code> to <code>.modal</code>, <code>aria-labelledby="myModalLabel"</code> attribute to reference the modal title, and <code>aria-hidden="true"</code> to tell assistive technologies to skip the modal's DOM elements.</p>
                                        <p>Additionally, you may give a description of your modal dialog with <code>aria-describedby</code> on <code>.modal</code>.</p>
                                    </div>
                                </div><!-- /panel-body -->
                                <table class="table table-bordered">
                                    <thead>
                                        <tr>
                                            <th>Available Type</th>
                                            <th>Demo</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>Basic Modal</td>
                                            <td><button type="button" class="btn btn-default" data-toggle="modal" data-target="#modalBasic">Show modal</button></td>
                                        </tr>
                                        <tr>
                                            <td>Modal Large</td>
                                            <td><button type="button" class="btn btn-default" data-toggle="modal" data-target="#modalLarge">Show modal</button></td>
                                        </tr>
                                        <tr>
                                            <td>Modal Small</td>
                                            <td><button type="button" class="btn btn-default" data-toggle="modal" data-target="#modalSmall">Show modal</button></td>
                                        </tr>
                                        <tr>
                                            <td>Remote Content</td>
                                            <td><a href="data-sample/modal-remote.html" data-scripts="data-sample/modal-remote.js" class="btn btn-default" data-toggle="modal" data-target="#modalRemote">Show modal</a></td>
                                        </tr>
                                        <tr>
                                            <td>Custom animated</td>
                                            <td><button type="button" class="btn btn-default" data-toggle="modal" data-target="#modalAnimated">Show modal</button></td>
                                        </tr>
                                        <tr>
                                            <td>Custom Width</td>
                                            <td><button type="button" class="btn btn-default" data-toggle="modal" data-target="#customWidth">Show modal</button></td>
                                        </tr>
                                        <tr>
                                            <td>Full Width</td>
                                            <td><button type="button" class="btn btn-default" data-toggle="modal" data-target="#fullWidth">Show modal</button></td>
                                        </tr>
                                        <tr>
                                            <td>Centering Modal</td>
                                            <td><button type="button" class="btn btn-default" data-toggle="modal" data-target="#centerModal">Show modal</button></td>
                                        </tr>
                                        <tr>
                                            <td>Customize Modal</td>
                                            <td>
                                                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#customModal1">Show modal</button>
                                                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#customModal2">Show modal</button>
                                                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#customModal3">Show modal</button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div><!-- /panel-modal -->
                            <!--MODAL DEMO-->
                            <!-- modalBasic -->
                            <div class="modal fade" id="modalBasic" tabindex="-1" role="dialog" aria-labelledby="modalBasicLabel" aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                            <h4 class="modal-title" id="modalBasicLabel">Basic Modal</h4>
                                        </div>
                                        <div class="modal-body">
                                            <p>Hello there, I'm a Modal! <i class="fa fa-smile-o"></i></p>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- modalLarge -->
                            <div class="modal fade" id="modalLarge" tabindex="-1" role="dialog" aria-labelledby="modalLargeLabel" aria-hidden="true">
                                <div class="modal-dialog modal-lg">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                            <h4 class="modal-title" id="modalLargeLabel">Modal Large <small><code>.modal-lg</code></small></h4>
                                        </div>
                                        <div class="modal-body">
                                            <p>Modals have two optional sizes, available via modifier classes to be placed on a <code>.modal-dialog</code>.</p>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- modalSmall -->
                            <div class="modal fade" id="modalSmall" tabindex="-1" role="dialog" aria-labelledby="modalSmallLabel" aria-hidden="true">
                                <div class="modal-dialog modal-sm">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                            <h4 class="modal-title" id="modalSmallLabel">Basic Modal</h4>
                                        </div>
                                        <div class="modal-body">
                                            <p>Modals have two optional sizes, available via modifier classes to be placed on a <code>.modal-dialog</code>.</p>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- modalRemote -->
                            <div class="modal fade" id="modalRemote" tabindex="-1" role="dialog" aria-labelledby="modalRemoteLabel" aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                            <h4 class="modal-title" id="modalRemoteLabel">Modal Remote</h4>
                                        </div>
                                        <div class="modal-body"></div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- modalAnimated -->
                            <div class="modal fade" data-sound="off" id="modalAnimated" tabindex="-1" role="dialog" aria-labelledby="modalAnimatedLabel" aria-hidden="true">
                                <div class="modal-dialog animated bounceIn">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                            <h4 class="modal-title" id="modalAnimatedLabel">Custom Animated <small>sound off</small></h4>
                                        </div>
                                        <div class="modal-body">
                                            Add animated classes to <code>.modal-dialog</code>, Support with all of animation <strong>In</strong> by animate.css.
                                            <pre class="prettyprint">&lt;div class=&quot;modal-dialog animated bounceIn&quot;&gt;...&lt;div&gt;</pre>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- customWidth Modal -->
                            <div class="modal fade" data-sound="bamboo" id="customWidth" tabindex="-1" role="dialog" aria-labelledby="customWidthLabel" aria-hidden="true">
                                <div class="modal-dialog animated flipInX" style="width:75%;">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                            <h4 class="modal-title" id="customWidthLabel">Custom Width <small>sound bamboo</small></h4>
                                        </div>
                                        <div class="modal-body">
                                            Inline CSS give you access to modify Modal width <code>style=&quot;width:75%&quot;</code>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- fullWidth Modal -->
                            <div class="modal modal-fullwidth fade" data-sound="complete" id="fullWidth" tabindex="-1" role="dialog" aria-labelledby="fullWidthLabel" aria-hidden="true">
                                <div class="modal-dialog animated flipInY">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                            <h4 class="modal-title" id="fullWidthLabel">Full Width <small>sound complete</small></h4>
                                        </div>
                                        <div class="modal-body">
                                            Just add <code>.modal.modal-fullwidth</code> to make Modal Full Width.
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- centerModal -->
                            <div class="modal modal-center fade" data-sound="note" id="centerModal" tabindex="-1" role="dialog" aria-labelledby="centerModalLabel" aria-hidden="true">
                                <div class="modal-dialog animated flipInX">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                            <h4 class="modal-title" id="centerModalLabel">Center Modal <small>sound note</small></h4>
                                        </div>
                                        <div class="modal-body">
                                            Just add <code>.modal.modal-center</code> to make Modal on middle of content (this mode use full width by default).
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- customModal1 -->
                            <div class="modal modal-center fade" data-sound="pulse" id="customModal1" tabindex="-1" role="dialog" aria-labelledby="customModal1Label" aria-hidden="true">
                                <div class="modal-dialog animated slideInDown">
                                    <div class="modal-content">
                                        <div class="modal-body">
                                            <p>You can play with <a rel="tooltip" title="Helper Classes" href="helper-classes.php" data-dismiss="modal" data-pjax=".content-body">Helper Classes</a> to customize a Modal. Enjoy It!</p>
                                            <p class="text-muted"><strong>Lorem ipsum</strong></p>
                                            <div class="callout callout-success">
                                                <h4>Customize a Modal <small class="text-muted">sound pulse</small></h4>
                                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde, eveniet distinctio placeat iste sit ducimus aperiam quis eum. Debitis, eaque, aliquam praesentium ab ullam quasi molestias amet dignissimos quae possimus.</p>
                                            </div>
                                            <div class="clearfix">
                                                <div class="pull-right">
                                                    <button type="button" class="btn btn-cloud" data-dismiss="modal">Close</button>
                                                    <button type="button" class="btn btn-success">Save changes</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- customModal2 -->
                            <div class="modal modal-center modal-fullwidth fade" id="customModal2" tabindex="-1" role="dialog" aria-labelledby="customModal2Label" aria-hidden="true">
                                <div class="modal-dialog animated bounceIn">
                                    <div class="modal-content bg-darknight">
                                        <div class="modal-body text-white">
                                            <p><strong>Holy guacamole!</strong> Best check yo self, you're not looking too good.</p>
                                            <form id="passwordCheck" action="#" class="form-inline" role="form">
                                                <div class="form-group">
                                                    <input type="password" class="form-control" placeholder="Type your password">
                                                </div>
                                            </form>
                                            <div class="clearfix">
                                                <div class="pull-right">
                                                    <button type="button" class="btn btn-sm btn-warning" data-dismiss="modal">Do this</button>
                                                    <button type="submit" form="passwordCheck" class="btn btn-sm btn-primary">Take Action</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->

                            <!-- customModal3 -->
                            <div class="modal modal-center fade" data-sound="sounds/synth" id="customModal3" tabindex="-1" role="dialog" aria-labelledby="customModal3Label" aria-hidden="true">
                                <div class="modal-dialog animated bounceIn">
                                    <div class="modal-content bg-danger">
                                        <div class="modal-body text-white">
                                            <h4>Oh snap! You got an error! <small class="text-cloud">sound custom value</small></h4>
                                            <p>Change this and that and try again. Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Cras mattis consectetur purus sit amet fermentum.</p>
                                            <p>
                                                <button type="button" class="btn btn-primary">Take this action</button>
                                                <button type="button" class="btn btn-default" data-dismiss="modal">Or do this</button>
                                            </p>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div><!-- /.modal -->
                        </div><!--/cols -->
                    </div><!--/row -->