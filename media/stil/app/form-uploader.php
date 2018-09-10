<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- UPLOADER
                    ================================================== -->
                    <!-- Dropzone -->
                    <div id="panel-dropzone" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-dropzone" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-dropzone" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-dropzone" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-dropzone" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Dropzone</h3>
                        </div><!-- /panel-heading -->

                        <form action="/target" data-input="dropzone" class="dropzone">
                            <div class="fallback">
                                <input name="mydropzone" type="file" multiple />
                            </div>
                        </form><!--/form-->    
                    </div><!-- /panel-dropzone -->



                    
                    <!-- Jasny File Input -->
                    <div id="panel-fileinput" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-fileinput" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-fileinput" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-fileinput" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-fileinput" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">File Input</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form action="#" role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="fileinput_widget">File input widgets</label>
                                    <div class="col-sm-5">
                                        <div class="fileinput fileinput-new" data-provides="fileinput">
                                            <div class="input-group">
                                                <div class="form-control uneditable-input span3" data-trigger="fileinput">
                                                    <i class="glyphicon glyphicon-file fileinput-exists"></i> 
                                                    <span class="fileinput-filename"></span>
                                                </div>
                                                <span class="input-group-btn">
                                                    <button class="btn btn-default fileinput-exists" rel="tooltip" title="remove" data-dismiss="fileinput"><i class="fa fa-times"></i></button>
                                                    <button class="btn btn-default btn-file">
                                                        <span class="fileinput-new">Select file</span>
                                                        <span class="fileinput-exists">Change</span>
                                                        <input type="file" name="fileinput_widget" id="fileinput_widget">
                                                    </button>
                                                </span>
                                            </div>
                                        </div><!-- /fileinput -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="fileinput_inline">File input inline</label>
                                    <div class="col-sm-5">
                                        <div class="fileinput fileinput-new" data-provides="fileinput">
                                            <span class="btn btn-icon btn-icon-right btn-primary btn-file">
                                                <i class="fa fa-upload"></i>
                                                <span class="fileinput-new">Select file</span>
                                                <span class="fileinput-exists">Change</span>
                                                <input type="file" name="fileinput_inline" id="fileinput_inline">
                                            </span>
                                            <span class="fileinput-filename"></span>
                                            <button class="close fileinput-exists" data-dismiss="fileinput" style="float: none">&times;</button>
                                        </div><!-- /fileinput -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="fileinput_thumb">Image upload widgets</label>
                                    <div class="col-sm-5">
                                        <div class="fileinput fileinput-new" data-provides="fileinput">
                                            <div class="fileinput-preview thumbnail" data-trigger="fileinput" style="width: 200px; height: 150px;">
                                                <img data-src="holder.js/100%x100%" alt="">
                                            </div>
                                            <div>
                                                <span class="btn btn-sm btn-icon btn-inverse btn-file">
                                                    <i class="fa fa-cloud-upload"></i>
                                                    <span class="fileinput-new">Select image</span>
                                                    <span class="fileinput-exists">Change</span>
                                                    <input type="file" name="fileinput_thumb" id="fileinput_thumb" accept="image/*">
                                                </span>
                                                <button class="btn btn-sm btn-icon btn-danger fileinput-exists" data-dismiss="fileinput">
                                                    <i class="fa fa-times"></i>
                                                    Remove
                                                </button>
                                            </div>
                                        </div><!-- /fileinput -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-fileinput -->