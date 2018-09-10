<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- Widget Panel
                    ================================================== -->
                    <div class="row">
                        <div class="col-md-6" data-toggle="sortable-widget">
                            <div id="panel-default" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-default" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-default" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-default" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-default" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Default panel</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>
                                        Widget Panel comes with four basic functions (close, collapse, expand, refresh). Panel allows you to enable support for <a rel="tooltip" title="View jquery-ui sortable doc" target="_blank" href="http://jqueryui.com/sortable/">jquery-ui sortable</a> by adding a class <code>.sortable-item</code> to Panel <i>(assuming you have added an attribute <code>data-toggle="sortable"</code> to the Panel parent)</i>. Click and drag Panel Icon to se how it work!
                                    </p>
                                    <p>How to make a basic Panel? Please see <a rel="tooltip" title="Bootstrap panel" target="_blank" href="http://getbootstrap.com/components/#panels">Bootstrap docs</a> about Panel.</p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer">
                                    Widget Panel <i>footer</i>
                                </div><!-- /panel-footer -->
                            </div><!-- /panel-default -->


                            <div id="panel-close" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-close="#panel-close" data-animate="hinge" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Panel close <small>actions</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>
                                        Panel actions close support with animate.css (only exits animation) by <strong>Dan Eden</strong>. Add attribute <code>data-animate="animateOutName"</code> to the action close button to activate custom animate close Panel.
                                    </p>
                                    <p>If you close the Panel it same you adding class <code>.hide</code> to Panel. Just remove class <code>.hide</code> to show it again.</p>
                                    <p>Support all of <a rel="tooltip" title="Animate.css" target="_blank" href="https://daneden.me/animate/">Animate.css</a></p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-close -->


                            <div id="panel-expand" class="panel panel-default">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <div class="btn-group">
                                            <button title="expand" class="btn-panel dropdown-toggle" data-toggle="dropdown">
                                                <i class="fa fa-expand"></i>
                                            </button>
                                            <ul class="dropdown-menu pull-right">
                                                <li><a href="#" data-expand="#panel-expand">Expand</a></li>
                                                <li><a href="#" data-expand="#panel-expand" data-expand-mode="fullscreen">Expand to fullscreen</a></li>
                                            </ul>
                                        </div>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars"></i> Expand <small>actions</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>Expand make a widget to toggle full window or fullscreen. Add attribute <code>data-expand="#panel-id"</code> to activate it, adding attribute <code>data-expand-mode="fullscreen"</code> to fullscreen mode. Expand feature also allow you to hide/show a element on screen toggle by adding class <code>.hide-on-expand</code> or <code>.show-on-expand</code></p>
                                    
                                    <div class="alert alert-success show-on-expand">
                                        <h4>This block show on expand</h4>
                                        <p>Commodo lobortis. Nascetur sed, fringilla dolor, etiam feugiat massa. Mauris tortor suspendisse, mauris etiam vitae. Quam in sunt. Tempor ultrices lacinia. Velit dis.</p>
                                    </div>
                                    <div class="alert alert-info hide-on-expand">
                                        <h4>This block hide on expand</h4>
                                        <p>Ridiculus tristique sed, feugiat tortor commodo. Mollis urna, ac hendrerit egestas, et adipiscing. Phasellus id pharetra. At dui, eget convallis, accumsan elementum. Adipiscing pellentesque. Purus vestibulum urna.</p>
                                    </div>
                                    <p>Fullscreen <a rel="tooltip" title="caniuse" href="http://caniuse.com/fullscreen" target="_parent">Support browsers</a>. <br><i>Safari 5.1 doesn't support use of the keyboard in fullscreen</i>.</p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer">
                                    Not allow <i>Sortable</i>
                                </div><!-- /panel-footer -->
                            </div><!-- /panel-expand -->


                            <div id="panel-table" class="panel panel-default">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-table" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-table" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-table" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-table" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars"></i> With table <small>no-sortable</small></h3>
                                </div><!-- /panel-heading -->

                                <!-- Table -->
                                <table class="tablesorter table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>First Name</th>
                                            <th>Last Name</th>
                                            <th>Username</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>1</td>
                                            <td>Mark</td>
                                            <td>Otto</td>
                                            <td>@mdo</td>
                                        </tr>
                                        <tr>
                                            <td>2</td>
                                            <td>Jacob</td>
                                            <td>Thornton</td>
                                            <td>@fat</td>
                                        </tr>
                                        <tr>
                                            <td>3</td>
                                            <td>Larry</td>
                                            <td>the Bird</td>
                                            <td>@twitter</td>
                                        </tr>
                                    </tbody>
                                    <tfoot>
                                        <tr>
                                            <th colspan="4" class="ts-pager form-horizontal">
                                                <button type="button" class="btn btn-default btn-sm first"><i class="icon-step-backward fa fa-angle-double-left"></i></button>
                                                <button type="button" class="btn btn-default btn-sm prev"><i class="icon-arrow-left fa fa-angle-left"></i></button>
                                                <span class="pagedisplay"></span> <!-- this can be any element, including an input -->
                                                <button type="button" class="btn btn-default btn-sm next"><i class="icon-arrow-right fa fa-angle-right"></i></button>
                                                <button type="button" class="btn btn-default btn-sm last"><i class="icon-step-forward fa fa-angle-double-right"></i></button>
                                                <select class="pagesize input-sm" title="Select page size">
                                                    <option value="5" selected>5</option>
                                                    <option value="10">10</option>
                                                    <option value="25">25</option>
                                                    <option value="50">50</option>
                                                </select>
                                                <select class="pagenum input-sm" title="Select page number"></select>
                                            </th>
                                        </tr>
                                    </tfoot>
                                </table><!-- /table -->

                                <div class="panel-footer hide-on-expand">Easily include <a rel="tooltip" title="Basic Table" data-pjax=".content-body" data-animatedpjax="fadeInUp" href="table-basic.php">table</a> within any Panel.</div>
                            </div><!-- /panel-table -->


                            <div id="panel-sortable" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-sortable" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-sortable" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-sortable" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-sortable" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Sortable handler</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magni, at, deserunt, eveniet, iure aperiam tempore facilis quam ut beatae dolores voluptate error voluptatibus quis minus repellendus qui commodi sint! Inventore.</p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-sortable -->


                            <div id="panel-withbtn" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="btn-group">
                                        <button rel="tooltip-bottom" title="copy" class="btn btn-default btn-sm"><i class="fa fa-copy"></i></button>
                                        <button rel="tooltip-bottom" title="cut" class="btn btn-default btn-sm"><i class="fa fa-cut"></i></button>
                                        <button rel="tooltip-bottom" title="paste" class="btn btn-default btn-sm"><i class="fa fa-paste"></i></button>
                                    </div><!-- /btn-group -->
                                    <div class="btn-group">
                                        <button rel="tooltip-bottom" title="create new file" class="btn btn-default btn-sm"><i class="fa fa-file"></i></button>
                                        <button rel="tooltip-bottom" title="open from folder" class="btn btn-default btn-sm"><i class="fa fa-folder-open-o"></i></button>
                                        <button rel="tooltip-bottom" title="save" class="btn btn-default btn-sm"><i class="fa fa-save"></i></button>
                                    </div><!-- /btn-group -->
                                    <h3 class="panel-title sortable-widget-handle">Play with button</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-helper-block">
                                    <button data-refresh="#panel-withbtn" rel="tooltip-bottom" title="refresh" class="btn btn-default btn-sm pull-right"><i class="fa fa-refresh"></i></button>
                                    <div class="btn-group" data-toggle="buttons">
                                        <button rel="tooltip-bottom" title="bold" class="btn btn-default btn-sm"><i class="fa fa-bold"></i></button>
                                        <button rel="tooltip-bottom" title="italic" class="btn btn-default btn-sm"><i class="fa fa-italic"></i></button>
                                        <button rel="tooltip-bottom" title="underline" class="btn btn-default btn-sm"><i class="fa fa-underline"></i></button>
                                        <button rel="tooltip-bottom" title="strikethrough" class="btn btn-default btn-sm"><i class="fa fa-strikethrough"></i></button>
                                    </div>
                                    <div class="btn-group">
                                        <button rel="tooltip-bottom" title="list-ol" class="btn btn-default btn-sm"><i class="fa fa-list-ol"></i></button>
                                        <button rel="tooltip-bottom" title="list-ul" class="btn btn-default btn-sm"><i class="fa fa-list-ul"></i></button>
                                        <button rel="tooltip-bottom" title="table" class="btn btn-default btn-sm"><i class="fa fa-table"></i></button>
                                    </div>
                                    <div class="btn-group" data-toggle="buttons">
                                        <button rel="tooltip-bottom" title="align-center" class="btn btn-default btn-sm"><i class="fa fa-align-center"></i></button>
                                        <button rel="tooltip-bottom" title="align-justify" class="btn btn-default btn-sm"><i class="fa fa-align-justify"></i></button>
                                        <button rel="tooltip-bottom" title="align-left" class="btn btn-default btn-sm"><i class="fa fa-align-left"></i></button>
                                        <button rel="tooltip-bottom" title="align-right" class="btn btn-default btn-sm"><i class="fa fa-align-right"></i></button>
                                    </div>
                                </div>
                                
                                <form class="single-editor" role="form">
                                    <textarea class="form-control single-editor" placeholder="Type something.."></textarea>
                                </form>
                                <div class="panel-body">
                                    <p>Easily Use button like a toolbar, best support with <code>.btn-sm</code> and <code>.btn-xs</code></p>
                                    <p>Please click on <strong>update</strong> button below!</p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer clearfix">
                                    <div class="pull-right">
                                        <button class="btn btn-warning btn-sm">Cancel</button>
                                        <button data-refresh="#panel-withbtn" class="btn btn-primary btn-sm">Update</button>
                                    </div>
                                </div>
                            </div><!-- /panel-withbtn -->
                        </div><!-- /cols -->



                        <div class="col-md-6" data-toggle="sortable-widget">
                            <div id="panel-context" class="panel panel-primary sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <div class="btn-group open">
                                            <button title="Chose a color" class="btn-panel disable-tooltip dropdown-toggle" data-toggle="dropdown">
                                                <i class="fa fa-tint"></i>
                                            </button>
                                            <ul class="dropdown-menu dropdown-inline bg-midnight pull-right" role="menu">
                                                <li>
                                                    <a rel="tooltip" title="Default" data-context="panel-default" data-target="#panel-context" class="color-pick bg-cloud"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Primary" data-context="panel-primary" data-target="#panel-context" class="color-pick bg-primary"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Success" data-context="panel-success" data-target="#panel-context" class="color-pick bg-success"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Info" data-context="panel-info" data-target="#panel-context" class="color-pick bg-info"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Warning" data-context="panel-warning" data-target="#panel-context" class="color-pick bg-warning"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Danger" data-context="panel-danger" data-target="#panel-context" class="color-pick bg-danger"></a>
                                                </li>
                                            </ul>
                                        </div>
                                        <button data-refresh="#panel-context" data-loader="loader-cloud" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-context" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-context" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-context" title="close" data-animate="flipOutX" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Contextual alternatives</h3>
                                </div><!-- /panel-heading -->
                                <div class="panel-body">
                                    <p>Easily make a panel more meaningful to a particular context by adding any of the contextual state classes (panel-primary, panel-success, panel-info, panel-warning, panel-danger). Please select a color to see contextual demo <i>(click on color chooser actions <span class="fa fa-tint"></span>)</i>.</p>
                                    <p>You can activate toggle contextual Panel by adding attributes <code>data-context="panel-context-class" data-target="#panel-id"</code> on your custom action.</p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer">
                                    Widget Panel <i>footer</i>
                                </div><!-- /panel-footer -->
                            </div><!-- /panel-context -->


                            <div id="panel-refresh" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <div class="btn-group">
                                            <button class="btn-panel dropdown-toggle" data-toggle="dropdown">
                                                <i class="fa fa-refresh"></i>
                                            </button>
                                            <ul class="dropdown-menu pull-right">
                                                <li>
                                                    <a href="#" data-refresh="#panel-refresh" data-url="data-sample/sample-plain-data.txt" data-target-place="#demo-target-refresh1">Basic Refresh</a>
                                                </li>
                                                <li>
                                                    <a href="#" data-refresh="#panel-refresh" data-url="data-sample/sample-data.json" data-loader="loader-cloud" data-target-place="#demo-target-refresh2">Advance Refresh</a>
                                                </li>
                                                <li class="divider"></li>
                                                <li>
                                                    <a href="#" data-refresh="#panel-refresh" data-url="data-sample/sample-datas.txt">Error case</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Panel refresh <small>actions</small></h3>
                                </div><!-- /panel-heading -->
                                <div class="panel-body">
                                    <div id="demo-target-refresh1"></div>
                                    <p>
                                        Panel actions refresh allow you to update data inside Panel via ajax. Just add <code>data-refresh="#panel-id"</code> and see how it work. Targeting action url via attribute <code>data-url="path/target/file"</code> and custom loader type with attribute <code>data-loader="loader-name"</code> (See avilable <a data-pjax=".content-body" href="loaders.php">Loaders</a>).
                                    </p>
                                    <p>By default data will replace on Panel Body <code>.panel-body</code>, But you can customize it with attribute <code>data-target-place="#target-place"</code></p>
                                    <p><strong>NOTE: </strong><i>Sometime, you may get an error message when refreshing a Panel. If your Panel have Panel body, error message will placed on there. But if you not have Panel Body on your Panel, error will placed after Panel Heading</i>.</p>
                                </div><!-- /panel-body -->
                                <table class="table table-hover" id="demo-target-refresh2"></table>
                            </div><!-- /panel-refresh -->


                            <div id="panel-collapse" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-collapse" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Collapse <small>actions</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>
                                        Collapse just hide the Panel Body, Table and List Group inside Panel. If your panel have a footer, its not include on hide elements. When you want make it or other elements include to collapse, just add class <code>.panel-collapse-element</code>. Add attribute <code>data-collapse="#panel-id"</code> to actions button.
                                    </p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-collapse -->


                            <div id="panel-collapse2" class="panel panel-default panel-collapsed sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-collapse2" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Default Collapse <small>actions</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>
                                        Add class <code>.panel-collapsed</code> to Panel when you want to collapse it by default.
                                    </p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer panel-collapse-element">Include to collapse element</div>
                            </div><!-- /panel-collapse2 -->


                            <div id="panel-scrollnice" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-scrollnice" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-scrollnice" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-scrollnice" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-scrollnice" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Scroll nice</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body" style="height:200px;" data-toggle="niceScroll" data-scroll-wrapper=".wrapper-scroll" data-scroll-cursorcolor="#ecf0f1">
                                    <div class="wrapper-scroll">
                                        <p>
                                            Just add attribute <code>data-toggle="niceScroll"</code> on Panel Body or other elements you want to make a Nice Scroll and define the scroll wrapper target <small>(required)</small> <code>data-scroll-wrapper=".wrapper-scroll"</code> <i>(can use with attribute class or id)</i>.
                                        </p>
                                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Possimus, dicta, sed quod veniam inventore nesciunt doloremque accusamus modi quasi tempore ratione excepturi cupiditate fuga iusto molestiae officiis saepe aperiam fugit qui neque culpa dolore aspernatur nemo totam quas dolorum dolor molestias autem quae quisquam.</p>
                                        <p> Consequatur, qui distinctio aperiam itaque sapiente amet quaerat hic. Quia, veritatis, assumenda, iste dolor laboriosam tenetur vitae neque illum sapiente esse expedita ipsum dolore tempora fugiat obcaecati consectetur facilis commodi fuga eveniet voluptates reprehenderit a culpa libero optio asperiores ad enim accusantium. Suscipit, aspernatur, laborum, ad cumque quos omnis quisquam inventore repudiandae fugiat alias aut qui?</p>
                                        <p> Consequatur, qui distinctio aperiam itaque sapiente amet quaerat hic. Quia, veritatis, assumenda, iste dolor laboriosam tenetur vitae neque illum sapiente esse expedita ipsum dolore tempora fugiat obcaecati consectetur facilis commodi fuga eveniet voluptates reprehenderit a culpa libero optio asperiores ad enim accusantium. Suscipit, aspernatur, laborum, ad cumque quos omnis quisquam inventore repudiandae fugiat alias aut qui?</p>
                                    </div>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-scrollnice -->


                            <div id="panel-listgroup" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-listgroup" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-listgroup" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-listgroup" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-listgroup" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> List group & slippylist</h3>
                                </div><!-- /panel-heading -->

                                <!-- List group -->
                                <ul class="list-group" data-toggle="slippylist">
                                    <li class="list-group-item">hold &amp; reorder</li>
                                    <li class="list-group-item no-reorder"><div class="badge pull-right">5</div>Swipe,</li>
                                    <li class="list-group-item no-swipe"><span class="slippylist-handle pull-right">or instantly</span> hold &amp; reorder</li>
                                    <li class="list-group-item">or either</li>
                                    <li class="list-group-item no-swipe no-reorder">or none of them.</li>
                                    <li class="list-group-item">Can play nicely with:</li>
                                    <li class="list-group-item">interaction <input style="position:relative;top:8px;margin-left:15px;" type="range" /></li>
                                    <li class="list-group-item" style="transform: scaleX(0.97) skewX(-10deg); -webkit-transform: scaleX(0.97) skewX(-10deg)">CSS transforms</li>
                                    <li class="list-group-item allow-select"><span class="no-reorder">and selectable text, even though animating elements with selected text is a bit weird.</span></li>
                                    <li class="list-group-item">iOS Safari</li>
                                    <li class="list-group-item">Android Firefox</li>
                                    <li class="list-group-item">Mobile Chrome</li>
                                    <li class="list-group-item">Oprea Presto and Blink</li>
                                </ul><!-- /list-group -->

                                <div class="panel-footer">Easily include full-width <a rel="tooltip" title="List Group" data-pjax=".content-body" data-animatedpjax="fadeInUp" href="navs-navbar.php#panel-listgroup">list groups</a> within any Panel.</div>
                            </div><!-- /panel-listgroup -->
                        </div><!-- /cols -->
                    </div><!-- /row -->