<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- BUTTONS
                    ================================================== -->
                    <div class="page-header">
                        <h1 id="buttons">Buttons & Paginations</h1>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-12" data-toggle="sortable-widget">
                            <div id="panel-btndemo" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-btndemo" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-btndemo" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-btndemo" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-btndemo" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Basic Buttons</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bordered-bottom">
                                    <p>Use any of the available button classes to quickly create a styled button <code>.btn</code>. Use the button classes on an <code>&lt;a&gt;</code>, <code>&lt;button&gt;</code>, or <code>&lt;input&gt;</code> element. Available class:</p> 
                                    <p><code>.btn-default</code> <code>.btn-inverse</code> <code>.btn-primary</code> <code>.btn-success</code> <code>.btn-info</code> <code>.btn-warning</code> <code>.btn-danger</code> <code>.btn-cloud</code> <code>.btn-silver</code> <code>.btn-link</code></p>
                                    <p class="text-muted"><strong>Options</strong></p>
                                    <button type="button" class="btn btn-default">Default</button>
                                    <button type="button" class="btn btn-inverse">Inverse</button>
                                    <button type="button" class="btn btn-primary">Primary</button>
                                    <button type="button" class="btn btn-success">Success</button>
                                    <button type="button" class="btn btn-info">Info</button>
                                    <button type="button" class="btn btn-warning">Warning</button>
                                    <button type="button" class="btn btn-danger">Danger</button>
                                    <button type="button" class="btn btn-cloud">Cloud</button>
                                    <button type="button" class="btn btn-silver">Silver</button>
                                    <button type="button" class="btn btn-link">Link</button>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Size</strong> <code>.btn-lg .btn-sm .btn-xs</code></p>
                                            <button type="button" class="btn btn-lg btn-default">Default</button>
                                            <button type="button" class="btn btn-inverse">Inverse</button>
                                            <button type="button" class="btn btn-sm btn-primary">Primary</button>
                                            <button type="button" class="btn btn-xs btn-success">Success</button>
                                        </div><!-- /cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Badge</strong> <code>.btn > .badge</code></p>
                                            <button type="button" class="btn btn-lg btn-default"><span class="badge">5</span> Default</button>
                                            <button type="button" class="btn btn-inverse"><span class="badge">6</span> Inverse</button>
                                            <button type="button" class="btn btn-sm btn-primary"><span class="badge">7</span> Primary</button>
                                            <button type="button" class="btn btn-xs btn-success"><span class="badge">8</span> Success</button>
                                        </div><!-- /cols -->
                                    </div><!-- /row -->
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Icon</strong> <code>.btn > .fa</code></p>
                                            <button type="button" class="btn btn-lg btn-default"><i class="fa fa-cog"></i> Settings</button>
                                            <button type="button" class="btn btn-inverse"><i class="fa fa-cog"></i> Settings</button>
                                            <button type="button" class="btn btn-sm btn-primary"><i class="fa fa-cog"></i> Settings</button>
                                            <button type="button" class="btn btn-xs btn-success"><i class="fa fa-cog"></i> Settings</button>
                                        </div><!-- /cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Alternative use with icons</strong></p>
                                            <div class="btn-group">
                                                <a class="btn btn-default" href="#"><i class="fa fa-user fa-fw"></i> User</a>
                                                <a class="btn btn-default dropdown-toggle" data-toggle="dropdown" href="#">
                                                    <span class="fa fa-caret-down"></span>
                                                </a>
                                                <ul class="dropdown-menu">
                                                    <li><a href="#"><i class="fa fa-pencil fa-fw"></i> Edit</a></li>
                                                    <li><a href="#"><i class="fa fa-trash-o fa-fw"></i> Delete</a></li>
                                                    <li><a href="#"><i class="fa fa-ban fa-fw"></i> Ban</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="#"><i class="fa fa-sign-out fa-fw"></i> Sign Out</a></li>
                                                </ul>
                                            </div>
                                        </div><!-- /cols -->
                                    </div><!-- /row -->
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Active state</strong> <code>.active</code></p>
                                            <button type="button" class="btn active btn-default">Default</button>
                                            <button type="button" class="btn active btn-inverse">Inverse</button>
                                            <button type="button" class="btn active btn-primary">Primary</button>
                                            <button type="button" class="btn active btn-success">Success</button>
                                        </div><!-- /cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Disabled state</strong> <code>disabled=&quot;disabled&quot;</code></p>
                                            <button type="button" class="btn btn-default" disabled>Default</button>
                                            <button type="button" class="btn btn-inverse" disabled>Inverse</button>
                                            <button type="button" class="btn btn-primary" disabled>Primary</button>
                                            <button type="button" class="btn btn-success" disabled>Success</button>
                                        </div><!-- /cols -->
                                    </div><!-- /row -->
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Rounded</strong> <code>.btn-rounded</code></p>
                                    <p>Best use with single button action, like a <strong>Call Action</strong>.</p>
                                    <button type="button" class="btn btn-rounded btn-lg btn-default">Default</button>
                                    <button type="button" class="btn btn-rounded btn-inverse">Inverse</button>
                                    <button type="button" class="btn btn-rounded btn-sm btn-primary">Primary</button>
                                    <button type="button" class="btn btn-rounded btn-xs btn-success" style="margin-right:20px">Success</button>

                                    <button type="button" class="btn btn-rounded btn-info">Info</button>
                                    <button type="button" class="btn btn-rounded btn-warning">Warning</button>
                                    <button type="button" class="btn btn-rounded btn-danger">Danger</button>
                                    <button type="button" class="btn btn-rounded btn-cloud">Cloud</button>
                                    <button type="button" class="btn btn-rounded btn-silver">Silver</button>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Buttons icon</strong> <code>.btn-icon</code></p>
                                            <p>
                                                <button class="btn btn-icon btn-lg btn-default">
                                                    <i class="fa fa-circle"></i>
                                                    Default
                                                </button>
                                                <button class="btn btn-icon btn-inverse">
                                                    <i class="fa fa-circle-o"></i>
                                                    Inverse
                                                </button>
                                                <button class="btn btn-icon btn-sm btn-primary">
                                                    <i class="fa fa-check"></i>
                                                    Primary
                                                </button>
                                                <button class="btn btn-icon btn-xs btn-danger">
                                                    <i class="fa fa-exclamation"></i>
                                                    Danger
                                                </button>
                                            </p>
                                        </div><!-- /cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Align</strong> <code>.btn-icon.btn-icon-right</code></p>
                                            <p>
                                                <button class="btn btn-icon btn-icon-right btn-xs btn-default">
                                                    <i class="fa fa-circle"></i>
                                                    Default
                                                </button>
                                                <button class="btn btn-icon btn-icon-right btn-sm btn-inverse">
                                                    <i class="fa fa-circle-o"></i>
                                                    Inverse
                                                </button>
                                                <button class="btn btn-icon btn-icon-right btn-primary">
                                                    <i class="fa fa-check"></i>
                                                    Primary
                                                </button>
                                                <button class="btn btn-icon btn-icon-right btn-lg btn-danger">
                                                    <i class="fa fa-exclamation"></i>
                                                    Danger
                                                </button>
                                            </p>
                                        </div><!-- /cols -->
                                    </div><!-- /row -->
                                    <br>
                                    <p>
                                        <button type="button" class="btn btn-icon btn-default">
                                            <i class="fa fa-circle"></i>
                                            Default
                                        </button>
                                        <button type="button" class="btn btn-icon btn-inverse">
                                            <i class="fa fa-circle-o"></i>
                                            Inverse
                                        </button>
                                        <button type="button" class="btn btn-icon btn-primary">
                                            <i class="fa fa-check"></i>
                                            Primary
                                        </button>
                                        <button type="button" class="btn btn-icon btn-success">
                                            <i class="fa fa-check-circle"></i>
                                            Success
                                        </button>
                                        <button type="button" class="btn btn-icon btn-info">
                                            <i class="fa fa-info"></i>
                                            Info
                                        </button>
                                        <button type="button" class="btn btn-icon btn-warning">
                                            <i class="fa fa-warning"></i>
                                            Warning
                                        </button>
                                        <button type="button" class="btn btn-icon btn-danger">
                                            <i class="fa fa-exclamation"></i>
                                            Danger
                                        </button>
                                        <button type="button" class="btn btn-icon btn-cloud">
                                            <i class="fa fa-cloud"></i>
                                            Cloud
                                        </button>
                                    </p>
                                </div><!-- /panel-body -->

                                <div class="panel-body">
                                    <p class="text-muted"><strong>Block level</strong> <code>.btn-block</code></p>
                                    <button type="button" class="btn btn-block btn-lg btn-default">Block level button</button>
                                    <button type="button" class="btn btn-block btn-lg btn-inverse">Block level button</button>
                                    <button type="button" class="btn btn-block btn-lg btn-primary">Block level button</button>
                                    <button type="button" class="btn btn-block btn-lg btn-success">Block level button</button>
                                </div><!-- /panel-body -->

                            </div><!-- /panel-btndemo -->
                        </div><!-- /cols -->
                    </div><!-- /row -->



                    <div class="row">
                        <div class="col-md-12" data-toggle="sortable-widget">
                            <div id="panel-btngroup" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-btngroup" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-btngroup" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-btngroup" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-btngroup" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Button groups & Dropdowns</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bordered-bottom">
                                    <p>Group a series of buttons together on a single line with the button group. Add on optional JavaScript radio and checkbox style behavior with <a rel="tooltip" title="Bootstrap buttons plugin" target="_blank" href="http://getbootstrap.com/javascript/#buttons">Bootstrap buttons plugin</a>.</p>
                                    <div class="callout callout-info">
                                        <h4>Tooltips &amp; popovers in button groups require special setting</h4>
                                        <p>When using tooltips or popovers on elements within a <code>.btn-group</code>, you'll have to specify the option <code>container: 'body'</code> to avoid unwanted side effects (such as the element growing wider and/or losing its rounded corners when the tooltip or popover is triggered).</p>
                                    </div>
                                    <p class="text-muted"><strong>Basic</strong></p>
                                    <div class="btn-group btn-group-lg">
                                        <button type="button" class="btn btn-default">Left</button>
                                        <button type="button" class="btn btn-default">Middle</button>
                                        <button type="button" class="btn btn-default">Right</button>
                                    </div>
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-inverse">Left</button>
                                        <button type="button" class="btn btn-inverse">Middle</button>
                                        <button type="button" class="btn btn-inverse">Right</button>
                                    </div>
                                    <div class="btn-group btn-group-sm">
                                        <button type="button" class="btn btn-primary">Left</button>
                                        <button type="button" class="btn btn-primary">Middle</button>
                                        <button type="button" class="btn btn-primary">Right</button>
                                    </div>
                                    <div class="btn-group btn-group-xs">
                                        <button type="button" class="btn btn-danger">Left</button>
                                        <button type="button" class="btn btn-danger">Middle</button>
                                        <button type="button" class="btn btn-danger">Right</button>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Nesting</strong></p>
                                    <div class="btn-group btn-group-lg">
                                        <button type="button" class="btn btn-default">Left</button>
                                        <button type="button" class="btn btn-default">Right</button>
                                        <div class="btn-group btn-group-lg">
                                            <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a href="#">Dropdown link</a></li>
                                                <li><a href="#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-inverse">Left</button>
                                        <button type="button" class="btn btn-inverse">Right</button>
                                        <div class="btn-group">
                                            <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a href="#">Dropdown link</a></li>
                                                <li><a href="#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="btn-group btn-group-sm">
                                        <button type="button" class="btn btn-primary">Left</button>
                                        <button type="button" class="btn btn-primary">Right</button>

                                        <div class="btn-group btn-group-sm">
                                            <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a href="#">Dropdown link</a></li>
                                                <li><a href="#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="btn-group btn-group-xs">
                                        <button type="button" class="btn btn-danger">Left</button>
                                        <button type="button" class="btn btn-danger">Right</button>
                                        <div class="btn-group btn-group-xs btn-group-xs">
                                            <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a href="#">Dropdown link</a></li>
                                                <li><a href="#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Toolbar</strong></p>
                                    <div class="btn-toolbar" role="toolbar">
                                        <div class="btn-group" data-toggle="buttons">
                                            <button rel="tooltip-bottom" title="bold" class="btn btn-default"><i class="fa fa-bold"></i></button>
                                            <button rel="tooltip-bottom" title="italic" class="btn btn-default"><i class="fa fa-italic"></i></button>
                                            <button rel="tooltip-bottom" title="underline" class="btn btn-default"><i class="fa fa-underline"></i></button>
                                            <button rel="tooltip-bottom" title="strikethrough" class="btn btn-default"><i class="fa fa-strikethrough"></i></button>
                                        </div>
                                        <div class="btn-group">
                                            <button rel="tooltip-bottom" title="list-ol" class="btn btn-default"><i class="fa fa-list-ol"></i></button>
                                            <button rel="tooltip-bottom" title="list-ul" class="btn btn-default"><i class="fa fa-list-ul"></i></button>
                                            <button rel="tooltip-bottom" title="table" class="btn btn-default"><i class="fa fa-table"></i></button>
                                        </div>
                                        <div class="btn-group" data-toggle="buttons">
                                            <button rel="tooltip-bottom" title="align-center" class="btn btn-default"><i class="fa fa-align-center"></i></button>
                                            <button rel="tooltip-bottom" title="align-justify" class="btn btn-default"><i class="fa fa-align-justify"></i></button>
                                            <button rel="tooltip-bottom" title="align-left" class="btn btn-default"><i class="fa fa-align-left"></i></button>
                                            <button rel="tooltip-bottom" title="align-right" class="btn btn-default"><i class="fa fa-align-right"></i></button>
                                        </div>
                                        <button data-refresh="#panel-btngroup" rel="tooltip-bottom" title="refresh" class="btn btn-default"><i class="fa fa-refresh"></i></button>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Justified</strong> <code>.btn-group-justified</code></p>
                                    <div class="callout callout-warning">
                                        <h4>Element-specific usage</h4>
                                        <p>This only works with <code>&lt;a&gt;</code> elements as the <code>&lt;button&gt;</code> doesn't pick up the styles we use to justify content (some <code>display: table-cell;</code>-fu).</p>
                                    </div>
                                    <div class="btn-group btn-group-justified">
                                        <a role="button" class="btn btn-default">Left</a>
                                        <a role="button" class="btn btn-default">Right</a>
                                        <div class="btn-group btn-group-lg">
                                            <a role="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </a>
                                            <ul class="dropdown-menu">
                                                <li><a href="#">Dropdown link</a></li>
                                                <li><a href="#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="btn-group btn-group-justified">
                                        <a role="button" class="btn btn-inverse">Left</a>
                                        <a role="button" class="btn btn-inverse">Right</a>
                                        <div class="btn-group btn-group-lg">
                                            <a role="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </a>
                                            <ul class="dropdown-menu">
                                                <li><a href="#">Dropdown link</a></li>
                                                <li><a href="#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="btn-group btn-group-justified">
                                        <a role="button" class="btn btn-primary">Left</a>
                                        <a role="button" class="btn btn-primary">Right</a>
                                        <div class="btn-group btn-group-lg">
                                            <a role="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </a>
                                            <ul class="dropdown-menu">
                                                <li><a href="#">Dropdown link</a></li>
                                                <li><a href="#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="btn-group btn-group-justified">
                                        <a role="button" class="btn btn-success">Left</a>
                                        <a role="button" class="btn btn-success">Right</a>
                                        <div class="btn-group btn-group-lg">
                                            <a role="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </a>
                                            <ul class="dropdown-menu">
                                                <li><a href="#">Dropdown link</a></li>
                                                <li><a href="#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Single button dropdowns & animated</strong></p>
                                    <div class="callout callout-danger">
                                        <h4>Plugin dependency</h4>
                                        <p>Button dropdowns require the <a rel="tooltip" title="Dropdown plugin" target="_blank" href="http://getbootstrap.com/javascript/#dropdowns">dropdown plugin</a> to be included in your version of Bootstrap. Support with all of <a rel="tooltip" title="animate.css" target="_blank" href="https://daneden.me/animate/">animate.css</a> (animate in type) by <strong>Dan Eden</strong>.</p>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                        Action <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu animated flipInX" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">
                                        Action <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu animated flipInY" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                        Action <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu animated bounceIn" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown">
                                        Action <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu animated fadeInLeft" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown">
                                        Pull right <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu pull-right animated fadeInLeft" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Split button dropdowns and dropup variation</strong></p>
                                    <!-- Split button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-default">Action</button>
                                        <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                            <i class="fa fa-angle-down"></i>
                                            <span class="sr-only">Toggle Dropdown</span>
                                        </button>
                                        <ul class="dropdown-menu animated lightSpeedIn" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Split button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-inverse">Action</button>
                                        <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">
                                            <i class="fa fa-angle-down"></i>
                                            <span class="sr-only">Toggle Dropdown</span>
                                        </button>
                                        <ul class="dropdown-menu animated rollIn" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Split button -->
                                    <div class="btn-group dropup">
                                        <button type="button" class="btn btn-primary">Action</button>
                                        <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                            <i class="fa fa-angle-up"></i>
                                            <span class="sr-only">Toggle Dropdown</span>
                                        </button>
                                        <ul class="dropdown-menu animated fadeInUp" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Split button -->
                                    <div class="btn-group dropup">
                                        <button type="button" class="btn btn-danger">Action</button>
                                        <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown">
                                            <i class="fa fa-angle-up"></i>
                                            <span class="sr-only">Toggle Dropdown</span>
                                        </button>
                                        <ul class="dropdown-menu animated rotateIn" role="menu">
                                            <li><a href="#">Action</a></li>
                                            <li><a href="#">Another action</a></li>
                                            <li><a href="#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="#">Separated link</a></li>
                                        </ul>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body">
                                    <p class="text-muted"><strong>Playing with icons</strong></p>
                                    <p>
                                        <button class="btn btn-default">
                                            <i class="fa fa-spinner fa-spin"></i>
                                        </button>
                                        <button class="btn btn-inverse">
                                            <i class="fa fa-refresh fa-spin"></i>
                                        </button>
                                        <button class="btn btn-primary" style="margin-right:20px;">
                                            <i class="fa fa-cog fa-spin"></i>
                                        </button>

                                        <button class="btn btn-cloud">
                                            <i class="fa fa-github"></i>
                                        </button>
                                        <button class="btn btn-success">
                                            <i class="fa fa-html5"></i>
                                        </button>
                                        <button class="btn btn-info">
                                            <i class="fa fa-twitter"></i>
                                        </button>
                                        <button class="btn btn-warning">
                                            <i class="fa fa-stack-overflow"></i>
                                        </button>
                                        <button class="btn btn-danger">
                                            <i class="fa fa-youtube-play"></i>
                                        </button>
                                        <button class="btn btn-silver">
                                            <i class="fa fa-google-plus"></i>
                                        </button>
                                    </p>
                                    <p>
                                        <a class="btn btn-lg btn-primary" target="_blank" href="https://wrapbootstrap.com/theme/stilearn-admin-template-WB0TFD2S0">
                                            <i class="fa fa-flag fa-3x pull-left"></i> Buy Stilearn Admin<br>Version 2.0
                                        </a>
                                    </p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-btngroup -->



                

                            <div id="panel-pagination" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-pagination" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-pagination" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-pagination" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-pagination" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Paginations</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Simple pagination</strong></p>
                                    <p>Fancy larger or smaller pagination? Add .pagination-lg or .pagination-sm for additional sizes.</p>
                                    <ul class="pagination pagination-sm">
                                        <li class="disabled"><a href="#">&laquo;</a></li>
                                        <li class="active"><a href="#">1</a></li>
                                        <li><a href="#">2</a></li>
                                        <li><a href="#">3</a></li>
                                        <li><a href="#">4</a></li>
                                        <li><a href="#">5</a></li>
                                        <li><a href="#">&raquo;</a></li>
                                    </ul>
                                    <ul class="pagination">
                                        <li class="disabled"><a href="#">&laquo;</a></li>
                                        <li class="active"><a href="#">1</a></li>
                                        <li><a href="#">2</a></li>
                                        <li><a href="#">3</a></li>
                                        <li><a href="#">4</a></li>
                                        <li><a href="#">5</a></li>
                                        <li><a href="#">&raquo;</a></li>
                                    </ul>
                                    <ul class="pagination pagination-lg">
                                        <li class="disabled"><a href="#">&laquo;</a></li>
                                        <li class="active"><a href="#">1</a></li>
                                        <li><a href="#">2</a></li>
                                        <li><a href="#">3</a></li>
                                        <li><a href="#">4</a></li>
                                        <li><a href="#">5</a></li>
                                        <li><a href="#">&raquo;</a></li>
                                    </ul>
                                </div><!-- /panel-body -->

                                <div class="panel-body">
                                    <p class="text-muted"><strong>Pager</strong></p>
                                    <p>Quick previous and next links for simple pagination implementations with light markup and styles. It's great for simple sites like blogs or magazines.</p>
                                    <ul class="pager">
                                        <li><a href="#">Previous</a></li>
                                        <li><a href="#">Next</a></li>
                                    </ul>

                                    <p class="text-muted"><strong>Aligned links</strong></p>
                                    <p>Alternatively, you can align each link to the sides:</p>
                                    <ul class="pager">
                                        <li class="previous"><a href="#">&larr; Older</a></li>
                                        <li class="next"><a href="#">Newer &rarr;</a></li>
                                    </ul>
                                    <p class="text-muted"><strong>Optional disabled state</strong></p>
                                    <p>Pager links also use the general <code>.disabled</code> utility class from the pagination.</p>
                                    <ul class="pager">
                                        <li class="previous disabled"><a href="#">&larr; Older</a></li>
                                        <li class="next"><a href="#">Newer &rarr;</a></li>
                                    </ul>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-pagination -->
                        </div><!-- /cols -->
                    </div><!-- /row -->