<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- LABEL & BADGE
                    ================================================== -->
                    <div class="row">
                        <div class="col-md-12">
                            <!-- LABEL & BADGE  -->
                            <div id="panel-labad" class="panel panel-default">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-labad" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-labad" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-labad" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-labad" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title">Labels & Badges</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p><strong>Labels</strong></p>
                                    <h1>Example heading <span class="label label-default">New</span></h1>
                                    <h2>Example heading <span class="label label-default">New</span></h2>
                                    <h3>Example heading <span class="label label-default">New</span></h3>
                                    <h4>Example heading <span class="label label-default">New</span></h4>
                                    <h5>Example heading <span class="label label-default">New</span></h5>
                                    <h6>Example heading <span class="label label-default">New</span></h6>
                                    <br>
                                    <p>Add any of the below mentioned modifier classes to change the appearance of a badge.</p>
                                    <p>
                                        <span class="label label-default">Default</span>
                                        <span class="label label-primary">Primary</span>
                                        <span class="label label-success">Success</span>
                                        <span class="label label-info">Info</span>
                                        <span class="label label-warning">Warning</span>
                                        <span class="label label-danger">Danger</span>
                                    </p>
                                    <pre class="no-padding prettyprint">&lt;span class=&quot;label label-default&quot;&gt;Default&lt;/span&gt;
&lt;span class=&quot;label label-primary&quot;&gt;Primary&lt;/span&gt;
&lt;span class=&quot;label label-success&quot;&gt;Success&lt;/span&gt;
&lt;span class=&quot;label label-info&quot;&gt;Info&lt;/span&gt;
&lt;span class=&quot;label label-warning&quot;&gt;Warning&lt;/span&gt;
&lt;span class=&quot;label label-danger&quot;&gt;Danger&lt;/span&gt;</pre>
                                </div><!-- /panel-body -->

                                <div class="panel-body">
                                    <p><strong>Badges</strong></p>
                                    <h1>Example heading <span class="badge badge-default">New</span></h1>
                                    <h2>Example heading <span class="badge badge-default">New</span></h2>
                                    <h3>Example heading <span class="badge badge-default">New</span></h3>
                                    <h4>Example heading <span class="badge badge-default">New</span></h4>
                                    <h5>Example heading <span class="badge badge-default">New</span></h5>
                                    <h6>Example heading <span class="badge badge-default">New</span></h6>
                                    <p>Add any of the below mentioned modifier classes to change the appearance of a label.</p>
                                    <p>
                                        <span class="badge badge-default">30</span>
                                        <span class="badge badge-primary">25</span>
                                        <span class="badge badge-success">20</span>
                                        <span class="badge badge-info">15</span>
                                        <span class="badge badge-warning">10</span>
                                        <span class="badge badge-danger">5</span>
                                    </p>
                                    <pre class="no-padding prettyprint">&lt;span class=&quot;badge badge-default&quot;&gt;30&lt;/span&gt;
&lt;span class=&quot;badge badge-primary&quot;&gt;25&lt;/span&gt;
&lt;span class=&quot;badge badge-success&quot;&gt;20&lt;/span&gt;
&lt;span class=&quot;badge badge-info&quot;&gt;15&lt;/span&gt;
&lt;span class=&quot;badge badge-warning&quot;&gt;10&lt;/span&gt;
&lt;span class=&quot;badge badge-danger&quot;&gt;5&lt;/span&gt;</pre>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-labad -->

                        </div><!--/cols -->
                    </div><!--/row -->