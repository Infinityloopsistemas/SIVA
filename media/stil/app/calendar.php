<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- CALENDAR
                    ====================== -->
                    <div class="row">
                    	<div class="col-md-9">
                    		<div class="panel panel-default">
                    			<div class="panel-heading bg-white">
                    				<div class="panel-actions">
                                        <button id="calendar-viewtoday" class="btn-panel">Today</button>
                                        <button id="calendar-viewmonth" class="btn-panel active">Month</button>
                                        <button id="calendar-viewweek" class="btn-panel">Week</button>
                                        <button id="calendar-viewday" class="btn-panel">Day</button>
                                    </div><!--panel-actions-->
                    				<h4 class="panel-title" id="calendar-viewtitle"><i class="fa fa-spinner fa-spin"></i></h4>
                    			</div><!--panel-heading-->

								<div class="panel-helper-block">
                    				<div class="btn-toolbar" role="toolbar">
                    					<div class="btn-group btn-group-sm pull-right">
									  		<button class="btn btn-default" id="calendar-viewnext">Next</button>
									  		<button class="btn btn-default" id="calendar-viewnextYear">Next Year</button>
                    					</div>
                    					<div class="btn-group btn-group-sm pull-left">
									  		<button class="btn btn-default" id="calendar-viewprevYear">Prev Year</button>
									  		<button class="btn btn-default" id="calendar-viewprev">Prev</button>
								  		</div>
									</div>
								</div><!--/panel-helper-block-->

                    			<div class="panel-body">
                    				<div id="calendar" class="table-responsive"></div>
                    			</div><!--panel-body-->
                    		</div><!--panel-->
                    	</div><!--cols-->

                    	<div class="col-md-3">
                    		<div id="external-events" class="panel panel-default">
                    			<div class="panel-heading bg-white">
                    				<div class="panel-actions">
                                        <button title="Add event" class="btn-panel disable-tooltip">
                                            <i class="fa fa-plus"></i>
                                        </button>
                                    </div><!--panel-actions-->
                    				<h4 class="panel-title">Draggable Events</h4>
                    			</div><!--panel-heading-->

                    			<div class="list-group">
                    				<div class='list-group-item external-event'>Consectetur adipisicing elit</div>
									<div class='list-group-item external-event'>Atque, illum, harum, delectus</div>
									<div class='list-group-item external-event'>Repudiandae quibusdam</div>
									<div class='list-group-item external-event'>Animi esse ratione quam</div>
									<div class='list-group-item external-event'>Quaerat suscipit itaque</div>
									<div class='list-group-item external-event'>Ut ipsa pariatur similique</div>
                    			</div><!--list-group-->

                    			<div class="panel-footer">
                    				<div class="nice-checkbox">
										<input type='checkbox' id='drop-remove' checked /> 
										<label for='drop-remove'>Remove after drop</label>
									</div>
                    			</div><!--panel-footer-->
                    		</div><!--panel-->
                    	</div><!--cols-->
                    </div><!--row-->
