(function($,undefined){var defaults={defaultView:'month',aspectRatio:1.35,header:{left:'title',center:'',right:'today prev,next'},weekends:true,allDayDefault:true,ignoreTimezone:true,lazyFetching:true,startParam:'start',endParam:'end',titleFormat:{month:'MMMM yyyy',week:"MMM d[ yyyy]{ '&#8212;'[ MMM] d yyyy}",day:'dddd, MMM d, yyyy'},columnFormat:{month:'ddd',week:'ddd M/d',day:'dddd M/d'},timeFormat:{'':'h(:mm)t'},isRTL:false,firstDay:0,monthNames:['Enero','February','March','April','May','June','July','August','September','October','November','December'],monthNamesShort:['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],dayNames:['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],dayNamesShort:['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],buttonText:{prev:'&nbsp;&#9668;&nbsp;',next:'&nbsp;&#9658;&nbsp;',prevYear:'&nbsp;&lt;&lt;&nbsp;',nextYear:'&nbsp;&gt;&gt;&nbsp;',today:'today',month:'month',week:'week',day:'day'},theme:false,buttonIcons:{prev:'circle-triangle-w',next:'circle-triangle-e'},unselectAuto:true,dropAccept:'*'};var rtlDefaults={header:{left:'next,prev today',center:'',right:'title'},buttonText:{prev:'&nbsp;&#9658;&nbsp;',next:'&nbsp;&#9668;&nbsp;',prevYear:'&nbsp;&gt;&gt;&nbsp;',nextYear:'&nbsp;&lt;&lt;&nbsp;'},buttonIcons:{prev:'circle-triangle-e',next:'circle-triangle-w'}};var fc=$.fullCalendar={version:"1.5.4"};var fcViews=fc.views={};$.fn.fullCalendar=function(options){if(typeof options=='string'){var args=Array.prototype.slice.call(arguments,1);var res;this.each(function(){var calendar=$.data(this,'fullCalendar');if(calendar&&$.isFunction(calendar[options])){var r=calendar[options].apply(calendar,args);if(res===undefined){res=r;}
if(options=='destroy'){$.removeData(this,'fullCalendar');}}});if(res!==undefined){return res;}
return this;}
var eventSources=options.eventSources||[];delete options.eventSources;if(options.events){eventSources.push(options.events);delete options.events;}
options=$.extend(true,{},defaults,(options.isRTL||options.isRTL===undefined&&defaults.isRTL)?rtlDefaults:{},options);this.each(function(i,_element){var element=$(_element);var calendar=new Calendar(element,options,eventSources);element.data('fullCalendar',calendar);calendar.render();});return this;};function setDefaults(d){$.extend(true,defaults,d);}
fc.setDefaults=setDefaults;function Calendar(element,options,eventSources){var t=this;t.options=options;t.render=render;t.destroy=destroy;t.refetchEvents=refetchEvents;t.reportEvents=reportEvents;t.reportEventChange=reportEventChange;t.rerenderEvents=rerenderEvents;t.changeView=changeView;t.select=select;t.unselect=unselect;t.prev=prev;t.next=next;t.prevYear=prevYear;t.nextYear=nextYear;t.today=today;t.gotoDate=gotoDate;t.incrementDate=incrementDate;t.formatDate=function(format,date){return formatDate(format,date,options)};t.formatDates=function(format,date1,date2){return formatDates(format,date1,date2,options)};t.getDate=getDate;t.getView=getView;t.option=option;t.trigger=trigger;EventManager.call(t,options,eventSources);var isFetchNeeded=t.isFetchNeeded;var fetchEvents=t.fetchEvents;var _element=element[0];var header;var headerElement;var content;var tm;var currentView;var viewInstances={};var elementOuterWidth;var suggestedViewHeight;var absoluteViewElement;var resizeUID=0;var ignoreWindowResize=0;var date=new Date();var events=[];var _dragElement;setYMD(date,options.year,options.month,options.date);function render(inc){if(!content){initialRender();}else{calcSize();markSizesDirty();markEventsDirty();renderView(inc);}}
function initialRender(){tm=options.theme?'ui':'fc';element.addClass('fc');if(options.isRTL){element.addClass('fc-rtl');}
if(options.theme){element.addClass('ui-widget');}
content=$("<div class='fc-content' style='position:relative'/>").prependTo(element);header=new Header(t,options);headerElement=header.render();if(headerElement){element.prepend(headerElement);}
changeView(options.defaultView);$(window).resize(windowResize);if(!bodyVisible()){lateRender();}}
function lateRender(){setTimeout(function(){if(!currentView.start&&bodyVisible()){renderView();}},0);}
function destroy(){$(window).unbind('resize',windowResize);header.destroy();content.remove();element.removeClass('fc fc-rtl ui-widget');}
function elementVisible(){return _element.offsetWidth!==0;}
function bodyVisible(){return $('body')[0].offsetWidth!==0;}
function changeView(newViewName){if(!currentView||newViewName!=currentView.name){ignoreWindowResize++;unselect();var oldView=currentView;var newViewElement;if(oldView){(oldView.beforeHide||noop)();setMinHeight(content,content.height());oldView.element.hide();}else{setMinHeight(content,1);}
content.css('overflow','hidden');currentView=viewInstances[newViewName];if(currentView){currentView.element.show();}else{currentView=viewInstances[newViewName]=new fcViews[newViewName](newViewElement=absoluteViewElement=$("<div class='fc-view fc-view-"+newViewName+"' style='position:absolute'/>").appendTo(content),t);}
if(oldView){header.deactivateButton(oldView.name);}
header.activateButton(newViewName);renderView();content.css('overflow','');if(oldView){setMinHeight(content,1);}
if(!newViewElement){(currentView.afterShow||noop)();}
ignoreWindowResize--;}}
function renderView(inc){if(elementVisible()){ignoreWindowResize++;unselect();if(suggestedViewHeight===undefined){calcSize();}
var forceEventRender=false;if(!currentView.start||inc||date<currentView.start||date>=currentView.end){currentView.render(date,inc||0);setSize(true);forceEventRender=true;}
else if(currentView.sizeDirty){currentView.clearEvents();setSize();forceEventRender=true;}
else if(currentView.eventsDirty){currentView.clearEvents();forceEventRender=true;}
currentView.sizeDirty=false;currentView.eventsDirty=false;updateEvents(forceEventRender);elementOuterWidth=element.outerWidth();header.updateTitle(currentView.title);var today=new Date();if(today>=currentView.start&&today<currentView.end){header.disableButton('today');}else{header.enableButton('today');}
ignoreWindowResize--;currentView.trigger('viewDisplay',_element);}}
function updateSize(){markSizesDirty();if(elementVisible()){calcSize();setSize();unselect();currentView.clearEvents();currentView.renderEvents(events);currentView.sizeDirty=false;}}
function markSizesDirty(){$.each(viewInstances,function(i,inst){inst.sizeDirty=true;});}
function calcSize(){if(options.contentHeight){suggestedViewHeight=options.contentHeight;}
else if(options.height){suggestedViewHeight=options.height-(headerElement?headerElement.height():0)-vsides(content);}
else{suggestedViewHeight=Math.round(content.width()/Math.max(options.aspectRatio,.5));}}
function setSize(dateChanged){ignoreWindowResize++;currentView.setHeight(suggestedViewHeight,dateChanged);if(absoluteViewElement){absoluteViewElement.css('position','relative');absoluteViewElement=null;}
currentView.setWidth(content.width(),dateChanged);ignoreWindowResize--;}
function windowResize(){if(!ignoreWindowResize){if(currentView.start){var uid=++resizeUID;setTimeout(function(){if(uid==resizeUID&&!ignoreWindowResize&&elementVisible()){if(elementOuterWidth!=(elementOuterWidth=element.outerWidth())){ignoreWindowResize++;updateSize();currentView.trigger('windowResize',_element);ignoreWindowResize--;}}},200);}else{lateRender();}}}
function updateEvents(forceRender){if(!options.lazyFetching||isFetchNeeded(currentView.visStart,currentView.visEnd)){refetchEvents();}
else if(forceRender){rerenderEvents();}}
function refetchEvents(){fetchEvents(currentView.visStart,currentView.visEnd);}
function reportEvents(_events){events=_events;rerenderEvents();}
function reportEventChange(eventID){rerenderEvents(eventID);}
function rerenderEvents(modifiedEventID){markEventsDirty();if(elementVisible()){currentView.clearEvents();currentView.renderEvents(events,modifiedEventID);currentView.eventsDirty=false;}}
function markEventsDirty(){$.each(viewInstances,function(i,inst){inst.eventsDirty=true;});}
function select(start,end,allDay){currentView.select(start,end,allDay===undefined?true:allDay);}
function unselect(){if(currentView){currentView.unselect();}}
function prev(){renderView(-1);}
function next(){renderView(1);}
function prevYear(){addYears(date,-1);renderView();}
function nextYear(){addYears(date,1);renderView();}
function today(){date=new Date();renderView();}
function gotoDate(year,month,dateOfMonth){if(year instanceof Date){date=cloneDate(year);}else{setYMD(date,year,month,dateOfMonth);}
renderView();}
function incrementDate(years,months,days){if(years!==undefined){addYears(date,years);}
if(months!==undefined){addMonths(date,months);}
if(days!==undefined){addDays(date,days);}
renderView();}
function getDate(){return cloneDate(date);}
function getView(){return currentView;}
function option(name,value){if(value===undefined){return options[name];}
if(name=='height'||name=='contentHeight'||name=='aspectRatio'){options[name]=value;updateSize();}}
function trigger(name,thisObj){if(options[name]){return options[name].apply(thisObj||_element,Array.prototype.slice.call(arguments,2));}}
if(options.droppable){$(document).bind('dragstart',function(ev,ui){var _e=ev.target;var e=$(_e);if(!e.parents('.fc').length){var accept=options.dropAccept;if($.isFunction(accept)?accept.call(_e,e):e.is(accept)){_dragElement=_e;currentView.dragStart(_dragElement,ev,ui);}}}).bind('dragstop',function(ev,ui){if(_dragElement){currentView.dragStop(_dragElement,ev,ui);_dragElement=null;}});}}
function Header(calendar,options){var t=this;t.render=render;t.destroy=destroy;t.updateTitle=updateTitle;t.activateButton=activateButton;t.deactivateButton=deactivateButton;t.disableButton=disableButton;t.enableButton=enableButton;var element=$([]);var tm;function render(){tm=options.theme?'ui':'fc';var sections=options.header;if(sections){element=$("<div class='fc-header' style='width:100%'/>").append($("<div/>").append(renderSection('left')).append(renderSection('center')).append(renderSection('right')));return element;}}
function destroy(){element.remove();}
function renderSection(position){var e=$("<span class='fc-header-"+position+"'/>");var buttonStr=options.header[position];if(buttonStr){$.each(buttonStr.split(' '),function(i){if(i>0){e.append("<span class='fc-header-space'/>");}
var prevButton;$.each(this.split(','),function(j,buttonName){if(buttonName=='title'){e.append("<span class='fc-header-title'><h2>&nbsp;</h2></span>");if(prevButton){prevButton.addClass(tm+'-corner-right');}
prevButton=null;}else{var buttonClick;if(calendar[buttonName]){buttonClick=calendar[buttonName];}
else if(fcViews[buttonName]){buttonClick=function(){button.removeClass(tm+'-state-hover');calendar.changeView(buttonName);};}
if(buttonClick){var icon=options.theme?smartProperty(options.buttonIcons,buttonName):null;var text=smartProperty(options.buttonText,buttonName);var button=$("<span class='fc-button fc-button-"+buttonName+" "+tm+"-state-default'>"+"<span class='fc-button-inner'>"+"<span class='fc-button-content'>"+
(icon?"<span class='fc-icon-wrap'>"+"<span class='ui-icon ui-icon-"+icon+"'/>"+"</span>":text)+"</span>"+"<span class='fc-button-effect'><span></span></span>"+"</span>"+"</span>");if(button){button.click(function(){if(!button.hasClass(tm+'-state-disabled')){buttonClick();}}).mousedown(function(){button.not('.'+tm+'-state-active').not('.'+tm+'-state-disabled').addClass(tm+'-state-down');}).mouseup(function(){button.removeClass(tm+'-state-down');}).hover(function(){button.not('.'+tm+'-state-active').not('.'+tm+'-state-disabled').addClass(tm+'-state-hover');},function(){button.removeClass(tm+'-state-hover').removeClass(tm+'-state-down');}).appendTo(e);if(!prevButton){button.addClass(tm+'-corner-left');}
prevButton=button;}}}});if(prevButton){prevButton.addClass(tm+'-corner-right');}});}
return e;}
function updateTitle(html){element.find('h2').html(html);}
function activateButton(buttonName){element.find('span.fc-button-'+buttonName).addClass(tm+'-state-active');}
function deactivateButton(buttonName){element.find('span.fc-button-'+buttonName).removeClass(tm+'-state-active');}
function disableButton(buttonName){element.find('span.fc-button-'+buttonName).addClass(tm+'-state-disabled');}
function enableButton(buttonName){element.find('span.fc-button-'+buttonName).removeClass(tm+'-state-disabled');}}
fc.sourceNormalizers=[];fc.sourceFetchers=[];var ajaxDefaults={dataType:'json',cache:false};var eventGUID=1;function EventManager(options,_sources){var t=this;t.isFetchNeeded=isFetchNeeded;t.fetchEvents=fetchEvents;t.addEventSource=addEventSource;t.removeEventSource=removeEventSource;t.updateEvent=updateEvent;t.renderEvent=renderEvent;t.removeEvents=removeEvents;t.clientEvents=clientEvents;t.normalizeEvent=normalizeEvent;var trigger=t.trigger;var getView=t.getView;var reportEvents=t.reportEvents;var stickySource={events:[]};var sources=[stickySource];var rangeStart,rangeEnd;var currentFetchID=0;var pendingSourceCnt=0;var loadingLevel=0;var cache=[];for(var i=0;i<_sources.length;i++){_addEventSource(_sources[i]);}
function isFetchNeeded(start,end){return!rangeStart||start<rangeStart||end>rangeEnd;}
function fetchEvents(start,end){rangeStart=start;rangeEnd=end;cache=[];var fetchID=++currentFetchID;var len=sources.length;pendingSourceCnt=len;for(var i=0;i<len;i++){fetchEventSource(sources[i],fetchID);}}
function fetchEventSource(source,fetchID){_fetchEventSource(source,function(events){if(fetchID==currentFetchID){if(events){for(var i=0;i<events.length;i++){events[i].source=source;normalizeEvent(events[i]);}
cache=cache.concat(events);}
pendingSourceCnt--;if(!pendingSourceCnt){reportEvents(cache);}}});}
function _fetchEventSource(source,callback){var i;var fetchers=fc.sourceFetchers;var res;for(i=0;i<fetchers.length;i++){res=fetchers[i](source,rangeStart,rangeEnd,callback);if(res===true){return;}
else if(typeof res=='object'){_fetchEventSource(res,callback);return;}}
var events=source.events;if(events){if($.isFunction(events)){pushLoading();events(cloneDate(rangeStart),cloneDate(rangeEnd),function(events){callback(events);popLoading();});}
else if($.isArray(events)){callback(events);}
else{callback();}}else{var url=source.url;if(url){var success=source.success;var error=source.error;var complete=source.complete;var data=$.extend({},source.data||{});var startParam=firstDefined(source.startParam,options.startParam);var endParam=firstDefined(source.endParam,options.endParam);if(startParam){data[startParam]=Math.round(+rangeStart/1000);}
if(endParam){data[endParam]=Math.round(+rangeEnd/1000);}
pushLoading();$.ajax($.extend({},ajaxDefaults,source,{data:data,success:function(events){events=events||[];var res=applyAll(success,this,arguments);if($.isArray(res)){events=res;}
callback(events);},error:function(){applyAll(error,this,arguments);callback();},complete:function(){applyAll(complete,this,arguments);popLoading();}}));}else{callback();}}}
function addEventSource(source){source=_addEventSource(source);if(source){pendingSourceCnt++;fetchEventSource(source,currentFetchID);}}
function _addEventSource(source){if($.isFunction(source)||$.isArray(source)){source={events:source};}
else if(typeof source=='string'){source={url:source};}
if(typeof source=='object'){normalizeSource(source);sources.push(source);return source;}}
function removeEventSource(source){sources=$.grep(sources,function(src){return!isSourcesEqual(src,source);});cache=$.grep(cache,function(e){return!isSourcesEqual(e.source,source);});reportEvents(cache);}
function updateEvent(event){var i,len=cache.length,e,defaultEventEnd=getView().defaultEventEnd,startDelta=event.start-event._start,endDelta=event.end?(event.end-(event._end||defaultEventEnd(event))):0;for(i=0;i<len;i++){e=cache[i];if(e._id==event._id&&e!=event){e.start=new Date(+e.start+startDelta);if(event.end){if(e.end){e.end=new Date(+e.end+endDelta);}else{e.end=new Date(+defaultEventEnd(e)+endDelta);}}else{e.end=null;}
e.title=event.title;e.url=event.url;e.allDay=event.allDay;e.className=event.className;e.editable=event.editable;e.color=event.color;e.backgroudColor=event.backgroudColor;e.borderColor=event.borderColor;e.textColor=event.textColor;normalizeEvent(e);}}
normalizeEvent(event);reportEvents(cache);}
function renderEvent(event,stick){normalizeEvent(event);if(!event.source){if(stick){stickySource.events.push(event);event.source=stickySource;}
cache.push(event);}
reportEvents(cache);}
function removeEvents(filter){if(!filter){cache=[];for(var i=0;i<sources.length;i++){if($.isArray(sources[i].events)){sources[i].events=[];}}}else{if(!$.isFunction(filter)){var id=filter+'';filter=function(e){return e._id==id;};}
cache=$.grep(cache,filter,true);for(var i=0;i<sources.length;i++){if($.isArray(sources[i].events)){sources[i].events=$.grep(sources[i].events,filter,true);}}}
reportEvents(cache);}
function clientEvents(filter){if($.isFunction(filter)){return $.grep(cache,filter);}
else if(filter){filter+='';return $.grep(cache,function(e){return e._id==filter;});}
return cache;}
function pushLoading(){if(!loadingLevel++){trigger('loading',null,true);}}
function popLoading(){if(!--loadingLevel){trigger('loading',null,false);}}
function normalizeEvent(event){var source=event.source||{};var ignoreTimezone=firstDefined(source.ignoreTimezone,options.ignoreTimezone);event._id=event._id||(event.id===undefined?'_fc'+eventGUID++:event.id+'');if(event.date){if(!event.start){event.start=event.date;}
delete event.date;}
event._start=cloneDate(event.start=parseDate(event.start,ignoreTimezone));event.end=parseDate(event.end,ignoreTimezone);if(event.end&&event.end<=event.start){event.end=null;}
event._end=event.end?cloneDate(event.end):null;if(event.allDay===undefined){event.allDay=firstDefined(source.allDayDefault,options.allDayDefault);}
if(event.className){if(typeof event.className=='string'){event.className=event.className.split(/\s+/);}}else{event.className=[];}}
function normalizeSource(source){if(source.className){if(typeof source.className=='string'){source.className=source.className.split(/\s+/);}}else{source.className=[];}
var normalizers=fc.sourceNormalizers;for(var i=0;i<normalizers.length;i++){normalizers[i](source);}}
function isSourcesEqual(source1,source2){return source1&&source2&&getSourcePrimitive(source1)==getSourcePrimitive(source2);}
function getSourcePrimitive(source){return((typeof source=='object')?(source.events||source.url):'')||source;}}
fc.addDays=addDays;fc.cloneDate=cloneDate;fc.parseDate=parseDate;fc.parseISO8601=parseISO8601;fc.parseTime=parseTime;fc.formatDate=formatDate;fc.formatDates=formatDates;var dayIDs=['sun','mon','tue','wed','thu','fri','sat'],DAY_MS=86400000,HOUR_MS=3600000,MINUTE_MS=60000;function addYears(d,n,keepTime){d.setFullYear(d.getFullYear()+n);if(!keepTime){clearTime(d);}
return d;}
function addMonths(d,n,keepTime){if(+d){var m=d.getMonth()+n,check=cloneDate(d);check.setDate(1);check.setMonth(m);d.setMonth(m);if(!keepTime){clearTime(d);}
while(d.getMonth()!=check.getMonth()){d.setDate(d.getDate()+(d<check?1:-1));}}
return d;}
function addDays(d,n,keepTime){if(+d){var dd=d.getDate()+n,check=cloneDate(d);check.setHours(9);check.setDate(dd);d.setDate(dd);if(!keepTime){clearTime(d);}
fixDate(d,check);}
return d;}
function fixDate(d,check){if(+d){while(d.getDate()!=check.getDate()){d.setTime(+d+(d<check?1:-1)*HOUR_MS);}}}
function addMinutes(d,n){d.setMinutes(d.getMinutes()+n);return d;}
function clearTime(d){d.setHours(0);d.setMinutes(0);d.setSeconds(0);d.setMilliseconds(0);return d;}
function cloneDate(d,dontKeepTime){if(dontKeepTime){return clearTime(new Date(+d));}
return new Date(+d);}
function zeroDate(){var i=0,d;do{d=new Date(1970,i++,1);}while(d.getHours());return d;}
function skipWeekend(date,inc,excl){inc=inc||1;while(!date.getDay()||(excl&&date.getDay()==1||!excl&&date.getDay()==6)){addDays(date,inc);}
return date;}
function dayDiff(d1,d2){return Math.round((cloneDate(d1,true)-cloneDate(d2,true))/DAY_MS);}
function setYMD(date,y,m,d){if(y!==undefined&&y!=date.getFullYear()){date.setDate(1);date.setMonth(0);date.setFullYear(y);}
if(m!==undefined&&m!=date.getMonth()){date.setDate(1);date.setMonth(m);}
if(d!==undefined){date.setDate(d);}}
function parseDate(s,ignoreTimezone){if(typeof s=='object'){return s;}
if(typeof s=='number'){return new Date(s*1000);}
if(typeof s=='string'){if(s.match(/^\d+(\.\d+)?$/)){return new Date(parseFloat(s)*1000);}
if(ignoreTimezone===undefined){ignoreTimezone=true;}
return parseISO8601(s,ignoreTimezone)||(s?new Date(s):null);}
return null;}
function parseISO8601(s,ignoreTimezone){var m=s.match(/^([0-9]{4})(-([0-9]{2})(-([0-9]{2})([T ]([0-9]{2}):([0-9]{2})(:([0-9]{2})(\.([0-9]+))?)?(Z|(([-+])([0-9]{2})(:?([0-9]{2}))?))?)?)?)?$/);if(!m){return null;}
var date=new Date(m[1],0,1);if(ignoreTimezone||!m[13]){var check=new Date(m[1],0,1,9,0);if(m[3]){date.setMonth(m[3]-1);check.setMonth(m[3]-1);}
if(m[5]){date.setDate(m[5]);check.setDate(m[5]);}
fixDate(date,check);if(m[7]){date.setHours(m[7]);}
if(m[8]){date.setMinutes(m[8]);}
if(m[10]){date.setSeconds(m[10]);}
if(m[12]){date.setMilliseconds(Number("0."+m[12])*1000);}
fixDate(date,check);}else{date.setUTCFullYear(m[1],m[3]?m[3]-1:0,m[5]||1);date.setUTCHours(m[7]||0,m[8]||0,m[10]||0,m[12]?Number("0."+m[12])*1000:0);if(m[14]){var offset=Number(m[16])*60+(m[18]?Number(m[18]):0);offset*=m[15]=='-'?1:-1;date=new Date(+date+(offset*60*1000));}}
return date;}
function parseTime(s){if(typeof s=='number'){return s*60;}
if(typeof s=='object'){return s.getHours()*60+s.getMinutes();}
var m=s.match(/(\d+)(?::(\d+))?\s*(\w+)?/);if(m){var h=parseInt(m[1],10);if(m[3]){h%=12;if(m[3].toLowerCase().charAt(0)=='p'){h+=12;}}
return h*60+(m[2]?parseInt(m[2],10):0);}}
function formatDate(date,format,options){return formatDates(date,null,format,options);}
function formatDates(date1,date2,format,options){options=options||defaults;var date=date1,otherDate=date2,i,len=format.length,c,i2,formatter,res='';for(i=0;i<len;i++){c=format.charAt(i);if(c=="'"){for(i2=i+1;i2<len;i2++){if(format.charAt(i2)=="'"){if(date){if(i2==i+1){res+="'";}else{res+=format.substring(i+1,i2);}
i=i2;}
break;}}}
else if(c=='('){for(i2=i+1;i2<len;i2++){if(format.charAt(i2)==')'){var subres=formatDate(date,format.substring(i+1,i2),options);if(parseInt(subres.replace(/\D/,''),10)){res+=subres;}
i=i2;break;}}}
else if(c=='['){for(i2=i+1;i2<len;i2++){if(format.charAt(i2)==']'){var subformat=format.substring(i+1,i2);var subres=formatDate(date,subformat,options);if(subres!=formatDate(otherDate,subformat,options)){res+=subres;}
i=i2;break;}}}
else if(c=='{'){date=date2;otherDate=date1;}
else if(c=='}'){date=date1;otherDate=date2;}
else{for(i2=len;i2>i;i2--){if(formatter=dateFormatters[format.substring(i,i2)]){if(date){res+=formatter(date,options);}
i=i2-1;break;}}
if(i2==i){if(date){res+=c;}}}}
return res;};var dateFormatters={s:function(d){return d.getSeconds()},ss:function(d){return zeroPad(d.getSeconds())},m:function(d){return d.getMinutes()},mm:function(d){return zeroPad(d.getMinutes())},h:function(d){return d.getHours()%12||12},hh:function(d){return zeroPad(d.getHours()%12||12)},H:function(d){return d.getHours()},HH:function(d){return zeroPad(d.getHours())},d:function(d){return d.getDate()},dd:function(d){return zeroPad(d.getDate())},ddd:function(d,o){return o.dayNamesShort[d.getDay()]},dddd:function(d,o){return o.dayNames[d.getDay()]},M:function(d){return d.getMonth()+1},MM:function(d){return zeroPad(d.getMonth()+1)},MMM:function(d,o){return o.monthNamesShort[d.getMonth()]},MMMM:function(d,o){return o.monthNames[d.getMonth()]},yy:function(d){return(d.getFullYear()+'').substring(2)},yyyy:function(d){return d.getFullYear()},t:function(d){return d.getHours()<12?'a':'p'},tt:function(d){return d.getHours()<12?'am':'pm'},T:function(d){return d.getHours()<12?'A':'P'},TT:function(d){return d.getHours()<12?'AM':'PM'},u:function(d){return formatDate(d,"yyyy-MM-dd'T'HH:mm:ss'Z'")},S:function(d){var date=d.getDate();if(date>10&&date<20){return'th';}
return['st','nd','rd'][date%10-1]||'th';}};fc.applyAll=applyAll;function exclEndDay(event){if(event.end){return _exclEndDay(event.end,event.allDay);}else{return addDays(cloneDate(event.start),1);}}
function _exclEndDay(end,allDay){end=cloneDate(end);return allDay||end.getHours()||end.getMinutes()?addDays(end,1):clearTime(end);}
function segCmp(a,b){return(b.msLength-a.msLength)*100+(a.event.start-b.event.start);}
function segsCollide(seg1,seg2){return seg1.end>seg2.start&&seg1.start<seg2.end;}
function sliceSegs(events,visEventEnds,start,end){var segs=[],i,len=events.length,event,eventStart,eventEnd,segStart,segEnd,isStart,isEnd;for(i=0;i<len;i++){event=events[i];eventStart=event.start;eventEnd=visEventEnds[i];if(eventEnd>start&&eventStart<end){if(eventStart<start){segStart=cloneDate(start);isStart=false;}else{segStart=eventStart;isStart=true;}
if(eventEnd>end){segEnd=cloneDate(end);isEnd=false;}else{segEnd=eventEnd;isEnd=true;}
segs.push({event:event,start:segStart,end:segEnd,isStart:isStart,isEnd:isEnd,msLength:segEnd-segStart});}}
return segs.sort(segCmp);}
function stackSegs(segs){var levels=[],i,len=segs.length,seg,j,collide,k;for(i=0;i<len;i++){seg=segs[i];j=0;while(true){collide=false;if(levels[j]){for(k=0;k<levels[j].length;k++){if(segsCollide(levels[j][k],seg)){collide=true;break;}}}
if(collide){j++;}else{break;}}
if(levels[j]){levels[j].push(seg);}else{levels[j]=[seg];}}
return levels;}
function lazySegBind(container,segs,bindHandlers){container.unbind('mouseover').mouseover(function(ev){var parent=ev.target,e,i,seg;while(parent!=this){e=parent;parent=parent.parentNode;}
if((i=e._fci)!==undefined){e._fci=undefined;seg=segs[i];bindHandlers(seg.event,seg.element,seg);$(ev.target).trigger(ev);}
ev.stopPropagation();});}
function setOuterWidth(element,width,includeMargins){for(var i=0,e;i<element.length;i++){e=$(element[i]);e.width(Math.max(0,width-hsides(e,includeMargins)));}}
function setOuterHeight(element,height,includeMargins){for(var i=0,e;i<element.length;i++){e=$(element[i]);e.height(Math.max(0,height-vsides(e,includeMargins)));}}
function hsides(element,includeMargins){return hpadding(element)+hborders(element)+(includeMargins?hmargins(element):0);}
function hpadding(element){return(parseFloat($.css(element[0],'paddingLeft',true))||0)+
(parseFloat($.css(element[0],'paddingRight',true))||0);}
function hmargins(element){return(parseFloat($.css(element[0],'marginLeft',true))||0)+
(parseFloat($.css(element[0],'marginRight',true))||0);}
function hborders(element){return(parseFloat($.css(element[0],'borderLeftWidth',true))||0)+
(parseFloat($.css(element[0],'borderRightWidth',true))||0);}
function vsides(element,includeMargins){return vpadding(element)+vborders(element)+(includeMargins?vmargins(element):0);}
function vpadding(element){return(parseFloat($.css(element[0],'paddingTop',true))||0)+
(parseFloat($.css(element[0],'paddingBottom',true))||0);}
function vmargins(element){return(parseFloat($.css(element[0],'marginTop',true))||0)+
(parseFloat($.css(element[0],'marginBottom',true))||0);}
function vborders(element){return(parseFloat($.css(element[0],'borderTopWidth',true))||0)+
(parseFloat($.css(element[0],'borderBottomWidth',true))||0);}
function setMinHeight(element,height){height=(typeof height=='number'?height+'px':height);element.each(function(i,_element){_element.style.cssText+=';min-height:'+height+';_height:'+height;});}
function noop(){}
function cmp(a,b){return a-b;}
function arrayMax(a){return Math.max.apply(Math,a);}
function zeroPad(n){return(n<10?'0':'')+n;}
function smartProperty(obj,name){if(obj[name]!==undefined){return obj[name];}
var parts=name.split(/(?=[A-Z])/),i=parts.length-1,res;for(;i>=0;i--){res=obj[parts[i].toLowerCase()];if(res!==undefined){return res;}}
return obj[''];}
function htmlEscape(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/'/g,'&#039;').replace(/"/g,'&quot;').replace(/\n/g,'<br />');}
function cssKey(_element){return _element.id+'/'+_element.className+'/'+_element.style.cssText.replace(/(^|;)\s*(top|left|width|height)\s*:[^;]*/ig,'');}
function disableTextSelection(element){element.attr('unselectable','on').css('MozUserSelect','none').bind('selectstart.ui',function(){return false;});}
function markFirstLast(e){e.children().removeClass('fc-first fc-last').filter(':first-child').addClass('fc-first').end().filter(':last-child').addClass('fc-last');}
function setDayID(cell,date){cell.each(function(i,_cell){_cell.className=_cell.className.replace(/^fc-\w*/,'fc-'+dayIDs[date.getDay()]);});}
function getSkinCss(event,opt){var source=event.source||{};var eventColor=event.color;var sourceColor=source.color;var optionColor=opt('eventColor');var backgroundColor=event.backgroundColor||eventColor||source.backgroundColor||sourceColor||opt('eventBackgroundColor')||optionColor;var borderColor=event.borderColor||eventColor||source.borderColor||sourceColor||opt('eventBorderColor')||optionColor;var textColor=event.textColor||source.textColor||opt('eventTextColor');var statements=[];if(backgroundColor){statements.push('background-color:'+backgroundColor);}
if(borderColor){statements.push('border-color:'+borderColor);}
if(textColor){statements.push('color:'+textColor);}
return statements.join(';');}
function applyAll(functions,thisObj,args){if($.isFunction(functions)){functions=[functions];}
if(functions){var i;var ret;for(i=0;i<functions.length;i++){ret=functions[i].apply(thisObj,args)||ret;}
return ret;}}
function firstDefined(){for(var i=0;i<arguments.length;i++){if(arguments[i]!==undefined){return arguments[i];}}}
fcViews.month=MonthView;function MonthView(element,calendar){var t=this;t.render=render;BasicView.call(t,element,calendar,'month');var opt=t.opt;var renderBasic=t.renderBasic;var formatDate=calendar.formatDate;function render(date,delta){if(delta){addMonths(date,delta);date.setDate(1);}
var start=cloneDate(date,true);start.setDate(1);var end=addMonths(cloneDate(start),1);var visStart=cloneDate(start);var visEnd=cloneDate(end);var firstDay=opt('firstDay');var nwe=opt('weekends')?0:1;if(nwe){skipWeekend(visStart);skipWeekend(visEnd,-1,true);}
addDays(visStart,-((visStart.getDay()-Math.max(firstDay,nwe)+7)%7));addDays(visEnd,(7-visEnd.getDay()+Math.max(firstDay,nwe))%7);var rowCnt=Math.round((visEnd-visStart)/(DAY_MS*7));if(opt('weekMode')=='fixed'){addDays(visEnd,(6-rowCnt)*7);rowCnt=6;}
t.title=formatDate(start,opt('titleFormat'));t.start=start;t.end=end;t.visStart=visStart;t.visEnd=visEnd;renderBasic(6,rowCnt,nwe?5:7,true);}}
fcViews.basicWeek=BasicWeekView;function BasicWeekView(element,calendar){var t=this;t.render=render;BasicView.call(t,element,calendar,'basicWeek');var opt=t.opt;var renderBasic=t.renderBasic;var formatDates=calendar.formatDates;function render(date,delta){if(delta){addDays(date,delta*7);}
var start=addDays(cloneDate(date),-((date.getDay()-opt('firstDay')+7)%7));var end=addDays(cloneDate(start),7);var visStart=cloneDate(start);var visEnd=cloneDate(end);var weekends=opt('weekends');if(!weekends){skipWeekend(visStart);skipWeekend(visEnd,-1,true);}
t.title=formatDates(visStart,addDays(cloneDate(visEnd),-1),opt('titleFormat'));t.start=start;t.end=end;t.visStart=visStart;t.visEnd=visEnd;renderBasic(1,1,weekends?7:5,false);}}
fcViews.basicDay=BasicDayView;function BasicDayView(element,calendar){var t=this;t.render=render;BasicView.call(t,element,calendar,'basicDay');var opt=t.opt;var renderBasic=t.renderBasic;var formatDate=calendar.formatDate;function render(date,delta){if(delta){addDays(date,delta);if(!opt('weekends')){skipWeekend(date,delta<0?-1:1);}}
t.title=formatDate(date,opt('titleFormat'));t.start=t.visStart=cloneDate(date,true);t.end=t.visEnd=addDays(cloneDate(t.start),1);renderBasic(1,1,1,false);}}
setDefaults({weekMode:'fixed'});function BasicView(element,calendar,viewName){var t=this;t.renderBasic=renderBasic;t.setHeight=setHeight;t.setWidth=setWidth;t.renderDayOverlay=renderDayOverlay;t.defaultSelectionEnd=defaultSelectionEnd;t.renderSelection=renderSelection;t.clearSelection=clearSelection;t.reportDayClick=reportDayClick;t.dragStart=dragStart;t.dragStop=dragStop;t.defaultEventEnd=defaultEventEnd;t.getHoverListener=function(){return hoverListener};t.colContentLeft=colContentLeft;t.colContentRight=colContentRight;t.dayOfWeekCol=dayOfWeekCol;t.dateCell=dateCell;t.cellDate=cellDate;t.cellIsAllDay=function(){return true};t.allDayRow=allDayRow;t.allDayBounds=allDayBounds;t.getRowCnt=function(){return rowCnt};t.getColCnt=function(){return colCnt};t.getColWidth=function(){return colWidth};t.getDaySegmentContainer=function(){return daySegmentContainer};View.call(t,element,calendar,viewName);OverlayManager.call(t);SelectionManager.call(t);BasicEventRenderer.call(t);var opt=t.opt;var trigger=t.trigger;var clearEvents=t.clearEvents;var renderOverlay=t.renderOverlay;var clearOverlays=t.clearOverlays;var daySelectionMousedown=t.daySelectionMousedown;var formatDate=calendar.formatDate;var head;var headCells;var body;var bodyRows;var bodyCells;var bodyFirstCells;var bodyCellTopInners;var daySegmentContainer;var viewWidth;var viewHeight;var colWidth;var rowCnt,colCnt;var coordinateGrid;var hoverListener;var colContentPositions;var rtl,dis,dit;var firstDay;var nwe;var tm;var colFormat;disableTextSelection(element.addClass('fc-grid'));function renderBasic(maxr,r,c,showNumbers){rowCnt=r;colCnt=c;updateOptions();var firstTime=!body;if(firstTime){buildSkeleton(maxr,showNumbers);}else{clearEvents();}
updateCells(firstTime);}
function updateOptions(){rtl=opt('isRTL');if(rtl){dis=-1;dit=colCnt-1;}else{dis=1;dit=0;}
firstDay=opt('firstDay');nwe=opt('weekends')?0:1;tm=opt('theme')?'ui':'fc';colFormat=opt('columnFormat');}
function buildSkeleton(maxRowCnt,showNumbers){var s;var headerClass=tm+"-widget-header";var contentClass=tm+"-widget-content";var i,j;var table;s="<table class='fc-border-separate' style='width:100%' cellspacing='0'>"+"<thead>"+"<tr>";for(i=0;i<colCnt;i++){s+="<th class='fc- "+headerClass+"'/>";}
s+="</tr>"+"</thead>"+"<tbody>";for(i=0;i<maxRowCnt;i++){s+="<tr class='fc-week"+i+"'>";for(j=0;j<colCnt;j++){s+="<td class='fc- "+contentClass+" fc-day"+(i*colCnt+j)+"'>"+"<div>"+
(showNumbers?"<div class='fc-day-number'/>":'')+"<div class='fc-day-content'>"+"<div style='position:relative'>&nbsp;</div>"+"</div>"+"</div>"+"</td>";}
s+="</tr>";}
s+="</tbody>"+"</table>";table=$(s).appendTo(element);head=table.find('thead');headCells=head.find('th');body=table.find('tbody');bodyRows=body.find('tr');bodyCells=body.find('td');bodyFirstCells=bodyCells.filter(':first-child');bodyCellTopInners=bodyRows.eq(0).find('div.fc-day-content div');markFirstLast(head.add(head.find('tr')));markFirstLast(bodyRows);bodyRows.eq(0).addClass('fc-first');dayBind(bodyCells);daySegmentContainer=$("<div style='position:absolute;z-index:8;top:0;left:0'/>").appendTo(element);}
function updateCells(firstTime){var dowDirty=firstTime||rowCnt==1;var month=t.start.getMonth();var today=clearTime(new Date());var cell;var date;var row;if(dowDirty){headCells.each(function(i,_cell){cell=$(_cell);date=indexDate(i);cell.html(formatDate(date,colFormat));setDayID(cell,date);});}
bodyCells.each(function(i,_cell){cell=$(_cell);date=indexDate(i);if(date.getMonth()==month){cell.removeClass('fc-other-month');}else{cell.addClass('fc-other-month');}
if(+date==+today){cell.addClass(tm+'-state-highlight fc-today');}else{cell.removeClass(tm+'-state-highlight fc-today');}
cell.find('div.fc-day-number').text(date.getDate());if(dowDirty){setDayID(cell,date);}});bodyRows.each(function(i,_row){row=$(_row);if(i<rowCnt){row.show();if(i==rowCnt-1){row.addClass('fc-last');}else{row.removeClass('fc-last');}}else{row.hide();}});}
function setHeight(height){viewHeight=height;var bodyHeight=viewHeight-head.height();var rowHeight;var rowHeightLast;var cell;if(opt('weekMode')=='variable'){rowHeight=rowHeightLast=Math.floor(bodyHeight/(rowCnt==1?2:6));}else{rowHeight=Math.floor(bodyHeight/rowCnt);rowHeightLast=bodyHeight-rowHeight*(rowCnt-1);}
bodyFirstCells.each(function(i,_cell){if(i<rowCnt){cell=$(_cell);setMinHeight(cell.find('> div'),(i==rowCnt-1?rowHeightLast:rowHeight)-vsides(cell));}});}
function setWidth(width){viewWidth=width;colContentPositions.clear();colWidth=Math.floor(viewWidth/colCnt);setOuterWidth(headCells.slice(0,-1),colWidth);}
function dayBind(days){days.click(dayClick).mousedown(daySelectionMousedown);}
function dayClick(ev){if(!opt('selectable')){var index=parseInt(this.className.match(/fc\-day(\d+)/)[1]);var date=indexDate(index);trigger('dayClick',this,date,true,ev);}}
function renderDayOverlay(overlayStart,overlayEnd,refreshCoordinateGrid){if(refreshCoordinateGrid){coordinateGrid.build();}
var rowStart=cloneDate(t.visStart);var rowEnd=addDays(cloneDate(rowStart),colCnt);for(var i=0;i<rowCnt;i++){var stretchStart=new Date(Math.max(rowStart,overlayStart));var stretchEnd=new Date(Math.min(rowEnd,overlayEnd));if(stretchStart<stretchEnd){var colStart,colEnd;if(rtl){colStart=dayDiff(stretchEnd,rowStart)*dis+dit+1;colEnd=dayDiff(stretchStart,rowStart)*dis+dit+1;}else{colStart=dayDiff(stretchStart,rowStart);colEnd=dayDiff(stretchEnd,rowStart);}
dayBind(renderCellOverlay(i,colStart,i,colEnd-1));}
addDays(rowStart,7);addDays(rowEnd,7);}}
function renderCellOverlay(row0,col0,row1,col1){var rect=coordinateGrid.rect(row0,col0,row1,col1,element);return renderOverlay(rect,element);}
function defaultSelectionEnd(startDate,allDay){return cloneDate(startDate);}
function renderSelection(startDate,endDate,allDay){renderDayOverlay(startDate,addDays(cloneDate(endDate),1),true);}
function clearSelection(){clearOverlays();}
function reportDayClick(date,allDay,ev){var cell=dateCell(date);var _element=bodyCells[cell.row*colCnt+cell.col];trigger('dayClick',_element,date,allDay,ev);}
function dragStart(_dragElement,ev,ui){hoverListener.start(function(cell){clearOverlays();if(cell){renderCellOverlay(cell.row,cell.col,cell.row,cell.col);}},ev);}
function dragStop(_dragElement,ev,ui){var cell=hoverListener.stop();clearOverlays();if(cell){var d=cellDate(cell);trigger('drop',_dragElement,d,true,ev,ui);}}
function defaultEventEnd(event){return cloneDate(event.start);}
coordinateGrid=new CoordinateGrid(function(rows,cols){var e,n,p;headCells.each(function(i,_e){e=$(_e);n=e.offset().left;if(i){p[1]=n;}
p=[n];cols[i]=p;});p[1]=n+e.outerWidth();bodyRows.each(function(i,_e){if(i<rowCnt){e=$(_e);n=e.offset().top;if(i){p[1]=n;}
p=[n];rows[i]=p;}});p[1]=n+e.outerHeight();});hoverListener=new HoverListener(coordinateGrid);colContentPositions=new HorizontalPositionCache(function(col){return bodyCellTopInners.eq(col);});function colContentLeft(col){return colContentPositions.left(col);}
function colContentRight(col){return colContentPositions.right(col);}
function dateCell(date){return{row:Math.floor(dayDiff(date,t.visStart)/7),col:dayOfWeekCol(date.getDay())};}
function cellDate(cell){return _cellDate(cell.row,cell.col);}
function _cellDate(row,col){return addDays(cloneDate(t.visStart),row*7+col*dis+dit);}
function indexDate(index){return _cellDate(Math.floor(index/colCnt),index%colCnt);}
function dayOfWeekCol(dayOfWeek){return((dayOfWeek-Math.max(firstDay,nwe)+colCnt)%colCnt)*dis+dit;}
function allDayRow(i){return bodyRows.eq(i);}
function allDayBounds(i){return{left:0,right:viewWidth};}}
function BasicEventRenderer(){var t=this;t.renderEvents=renderEvents;t.compileDaySegs=compileSegs;t.clearEvents=clearEvents;t.bindDaySeg=bindDaySeg;DayEventRenderer.call(t);var opt=t.opt;var trigger=t.trigger;var isEventDraggable=t.isEventDraggable;var isEventResizable=t.isEventResizable;var reportEvents=t.reportEvents;var reportEventClear=t.reportEventClear;var eventElementHandlers=t.eventElementHandlers;var showEvents=t.showEvents;var hideEvents=t.hideEvents;var eventDrop=t.eventDrop;var getDaySegmentContainer=t.getDaySegmentContainer;var getHoverListener=t.getHoverListener;var renderDayOverlay=t.renderDayOverlay;var clearOverlays=t.clearOverlays;var getRowCnt=t.getRowCnt;var getColCnt=t.getColCnt;var renderDaySegs=t.renderDaySegs;var resizableDayEvent=t.resizableDayEvent;function renderEvents(events,modifiedEventId){reportEvents(events);renderDaySegs(compileSegs(events),modifiedEventId);}
function clearEvents(){reportEventClear();getDaySegmentContainer().empty();}
function compileSegs(events){var rowCnt=getRowCnt(),colCnt=getColCnt(),d1=cloneDate(t.visStart),d2=addDays(cloneDate(d1),colCnt),visEventsEnds=$.map(events,exclEndDay),i,row,j,level,k,seg,segs=[];for(i=0;i<rowCnt;i++){row=stackSegs(sliceSegs(events,visEventsEnds,d1,d2));for(j=0;j<row.length;j++){level=row[j];for(k=0;k<level.length;k++){seg=level[k];seg.row=i;seg.level=j;segs.push(seg);}}
addDays(d1,7);addDays(d2,7);}
return segs;}
function bindDaySeg(event,eventElement,seg){if(isEventDraggable(event)){draggableDayEvent(event,eventElement);}
if(seg.isEnd&&isEventResizable(event)){resizableDayEvent(event,eventElement,seg);}
eventElementHandlers(event,eventElement);}
function draggableDayEvent(event,eventElement){var hoverListener=getHoverListener();var dayDelta;eventElement.draggable({zIndex:9,delay:50,opacity:opt('dragOpacity'),revertDuration:opt('dragRevertDuration'),start:function(ev,ui){trigger('eventDragStart',eventElement,event,ev,ui);hideEvents(event,eventElement);hoverListener.start(function(cell,origCell,rowDelta,colDelta){eventElement.draggable('option','revert',!cell||!rowDelta&&!colDelta);clearOverlays();if(cell){dayDelta=rowDelta*7+colDelta*(opt('isRTL')?-1:1);renderDayOverlay(addDays(cloneDate(event.start),dayDelta),addDays(exclEndDay(event),dayDelta));}else{dayDelta=0;}},ev,'drag');},stop:function(ev,ui){hoverListener.stop();clearOverlays();trigger('eventDragStop',eventElement,event,ev,ui);if(dayDelta){eventDrop(this,event,dayDelta,0,event.allDay,ev,ui);}else{eventElement.css('filter','');showEvents(event,eventElement);}}});}}
fcViews.agendaWeek=AgendaWeekView;function AgendaWeekView(element,calendar){var t=this;t.render=render;AgendaView.call(t,element,calendar,'agendaWeek');var opt=t.opt;var renderAgenda=t.renderAgenda;var formatDates=calendar.formatDates;function render(date,delta){if(delta){addDays(date,delta*7);}
var start=addDays(cloneDate(date),-((date.getDay()-opt('firstDay')+7)%7));var end=addDays(cloneDate(start),7);var visStart=cloneDate(start);var visEnd=cloneDate(end);var weekends=opt('weekends');if(!weekends){skipWeekend(visStart);skipWeekend(visEnd,-1,true);}
t.title=formatDates(visStart,addDays(cloneDate(visEnd),-1),opt('titleFormat'));t.start=start;t.end=end;t.visStart=visStart;t.visEnd=visEnd;renderAgenda(weekends?7:5);}}
fcViews.agendaDay=AgendaDayView;function AgendaDayView(element,calendar){var t=this;t.render=render;AgendaView.call(t,element,calendar,'agendaDay');var opt=t.opt;var renderAgenda=t.renderAgenda;var formatDate=calendar.formatDate;function render(date,delta){if(delta){addDays(date,delta);if(!opt('weekends')){skipWeekend(date,delta<0?-1:1);}}
var start=cloneDate(date,true);var end=addDays(cloneDate(start),1);t.title=formatDate(date,opt('titleFormat'));t.start=t.visStart=start;t.end=t.visEnd=end;renderAgenda(1);}}
setDefaults({allDaySlot:true,allDayText:'all-day',firstHour:6,slotMinutes:30,defaultEventMinutes:120,axisFormat:'h(:mm)tt',timeFormat:{agenda:'h:mm{ - h:mm}'},dragOpacity:{agenda:.5},minTime:0,maxTime:24});function AgendaView(element,calendar,viewName){var t=this;t.renderAgenda=renderAgenda;t.setWidth=setWidth;t.setHeight=setHeight;t.beforeHide=beforeHide;t.afterShow=afterShow;t.defaultEventEnd=defaultEventEnd;t.timePosition=timePosition;t.dayOfWeekCol=dayOfWeekCol;t.dateCell=dateCell;t.cellDate=cellDate;t.cellIsAllDay=cellIsAllDay;t.allDayRow=getAllDayRow;t.allDayBounds=allDayBounds;t.getHoverListener=function(){return hoverListener};t.colContentLeft=colContentLeft;t.colContentRight=colContentRight;t.getDaySegmentContainer=function(){return daySegmentContainer};t.getSlotSegmentContainer=function(){return slotSegmentContainer};t.getMinMinute=function(){return minMinute};t.getMaxMinute=function(){return maxMinute};t.getBodyContent=function(){return slotContent};t.getRowCnt=function(){return 1};t.getColCnt=function(){return colCnt};t.getColWidth=function(){return colWidth};t.getSlotHeight=function(){return slotHeight};t.defaultSelectionEnd=defaultSelectionEnd;t.renderDayOverlay=renderDayOverlay;t.renderSelection=renderSelection;t.clearSelection=clearSelection;t.reportDayClick=reportDayClick;t.dragStart=dragStart;t.dragStop=dragStop;View.call(t,element,calendar,viewName);OverlayManager.call(t);SelectionManager.call(t);AgendaEventRenderer.call(t);var opt=t.opt;var trigger=t.trigger;var clearEvents=t.clearEvents;var renderOverlay=t.renderOverlay;var clearOverlays=t.clearOverlays;var reportSelection=t.reportSelection;var unselect=t.unselect;var daySelectionMousedown=t.daySelectionMousedown;var slotSegHtml=t.slotSegHtml;var formatDate=calendar.formatDate;var dayTable;var dayHead;var dayHeadCells;var dayBody;var dayBodyCells;var dayBodyCellInners;var dayBodyFirstCell;var dayBodyFirstCellStretcher;var slotLayer;var daySegmentContainer;var allDayTable;var allDayRow;var slotScroller;var slotContent;var slotSegmentContainer;var slotTable;var slotTableFirstInner;var axisFirstCells;var gutterCells;var selectionHelper;var viewWidth;var viewHeight;var axisWidth;var colWidth;var gutterWidth;var slotHeight;var savedScrollTop;var colCnt;var slotCnt;var coordinateGrid;var hoverListener;var colContentPositions;var slotTopCache={};var tm;var firstDay;var nwe;var rtl,dis,dit;var minMinute,maxMinute;var colFormat;disableTextSelection(element.addClass('fc-agenda'));function renderAgenda(c){colCnt=c;updateOptions();if(!dayTable){buildSkeleton();}else{clearEvents();}
updateCells();}
function updateOptions(){tm=opt('theme')?'ui':'fc';nwe=opt('weekends')?0:1;firstDay=opt('firstDay');if(rtl=opt('isRTL')){dis=-1;dit=colCnt-1;}else{dis=1;dit=0;}
minMinute=parseTime(opt('minTime'));maxMinute=parseTime(opt('maxTime'));colFormat=opt('columnFormat');}
function buildSkeleton(){var headerClass=tm+"-widget-header";var contentClass=tm+"-widget-content";var s;var i;var d;var maxd;var minutes;var slotNormal=opt('slotMinutes')%15==0;s="<table style='width:100%' class='fc-agenda-days fc-border-separate' cellspacing='0'>"+"<thead>"+"<tr>"+"<th class='fc-agenda-axis "+headerClass+"'>&nbsp;</th>";for(i=0;i<colCnt;i++){s+="<th class='fc- fc-col"+i+' '+headerClass+"'/>";}
s+="<th class='fc-agenda-gutter "+headerClass+"'>&nbsp;</th>"+"</tr>"+"</thead>"+"<tbody>"+"<tr>"+"<th class='fc-agenda-axis "+headerClass+"'>&nbsp;</th>";for(i=0;i<colCnt;i++){s+="<td class='fc- fc-col"+i+' '+contentClass+"'>"+"<div>"+"<div class='fc-day-content'>"+"<div style='position:relative'>&nbsp;</div>"+"</div>"+"</div>"+"</td>";}
s+="<td class='fc-agenda-gutter "+contentClass+"'>&nbsp;</td>"+"</tr>"+"</tbody>"+"</table>";dayTable=$(s).appendTo(element);dayHead=dayTable.find('thead');dayHeadCells=dayHead.find('th').slice(1,-1);dayBody=dayTable.find('tbody');dayBodyCells=dayBody.find('td').slice(0,-1);dayBodyCellInners=dayBodyCells.find('div.fc-day-content div');dayBodyFirstCell=dayBodyCells.eq(0);dayBodyFirstCellStretcher=dayBodyFirstCell.find('> div');markFirstLast(dayHead.add(dayHead.find('tr')));markFirstLast(dayBody.add(dayBody.find('tr')));axisFirstCells=dayHead.find('th:first');gutterCells=dayTable.find('.fc-agenda-gutter');slotLayer=$("<div style='position:absolute;z-index:2;left:0;width:100%'/>").appendTo(element);if(opt('allDaySlot')){daySegmentContainer=$("<div style='position:absolute;z-index:8;top:0;left:0'/>").appendTo(slotLayer);s="<table style='width:100%' class='fc-agenda-allday' cellspacing='0'>"+"<tr>"+"<th class='"+headerClass+" fc-agenda-axis'>"+opt('allDayText')+"</th>"+"<td>"+"<div class='fc-day-content'><div style='position:relative'/></div>"+"</td>"+"<th class='"+headerClass+" fc-agenda-gutter'>&nbsp;</th>"+"</tr>"+"</table>";allDayTable=$(s).appendTo(slotLayer);allDayRow=allDayTable.find('tr');dayBind(allDayRow.find('td'));axisFirstCells=axisFirstCells.add(allDayTable.find('th:first'));gutterCells=gutterCells.add(allDayTable.find('th.fc-agenda-gutter'));slotLayer.append("<div class='fc-agenda-divider "+headerClass+"'>"+"<div class='fc-agenda-divider-inner'/>"+"</div>");}else{daySegmentContainer=$([]);}
slotScroller=$("<div style='position:absolute;width:100%;overflow-x:hidden;overflow-y:auto'/>").appendTo(slotLayer);slotContent=$("<div style='position:relative;width:100%;overflow:hidden'/>").appendTo(slotScroller);slotSegmentContainer=$("<div style='position:absolute;z-index:8;top:0;left:0'/>").appendTo(slotContent);s="<table class='fc-agenda-slots' style='width:100%' cellspacing='0'>"+"<tbody>";d=zeroDate();maxd=addMinutes(cloneDate(d),maxMinute);addMinutes(d,minMinute);slotCnt=0;for(i=0;d<maxd;i++){minutes=d.getMinutes();s+="<tr class='fc-slot"+i+' '+(!minutes?'':'fc-minor')+"'>"+"<th class='fc-agenda-axis "+headerClass+"'>"+
((!slotNormal||!minutes)?formatDate(d,opt('axisFormat')):'&nbsp;')+"</th>"+"<td class='"+contentClass+"'>"+"<div style='position:relative'>&nbsp;</div>"+"</td>"+"</tr>";addMinutes(d,opt('slotMinutes'));slotCnt++;}
s+="</tbody>"+"</table>";slotTable=$(s).appendTo(slotContent);slotTableFirstInner=slotTable.find('div:first');slotBind(slotTable.find('td'));axisFirstCells=axisFirstCells.add(slotTable.find('th:first'));}
function updateCells(){var i;var headCell;var bodyCell;var date;var today=clearTime(new Date());for(i=0;i<colCnt;i++){date=colDate(i);headCell=dayHeadCells.eq(i);headCell.html(formatDate(date,colFormat));bodyCell=dayBodyCells.eq(i);if(+date==+today){bodyCell.addClass(tm+'-state-highlight fc-today');}else{bodyCell.removeClass(tm+'-state-highlight fc-today');}
setDayID(headCell.add(bodyCell),date);}}
function setHeight(height,dateChanged){if(height===undefined){height=viewHeight;}
viewHeight=height;slotTopCache={};var headHeight=dayBody.position().top;var allDayHeight=slotScroller.position().top;var bodyHeight=Math.min(height-headHeight,slotTable.height()+allDayHeight+1);dayBodyFirstCellStretcher.height(bodyHeight-vsides(dayBodyFirstCell));slotLayer.css('top',headHeight);slotScroller.height(bodyHeight-allDayHeight-1);slotHeight=slotTableFirstInner.height()+1;if(dateChanged){resetScroll();}}
function setWidth(width){viewWidth=width;colContentPositions.clear();axisWidth=0;setOuterWidth(axisFirstCells.width('').each(function(i,_cell){axisWidth=Math.max(axisWidth,$(_cell).outerWidth());}),axisWidth);var slotTableWidth=slotScroller[0].clientWidth;gutterWidth=slotScroller.width()-slotTableWidth;if(gutterWidth){setOuterWidth(gutterCells,gutterWidth);gutterCells.show().prev().removeClass('fc-last');}else{gutterCells.hide().prev().addClass('fc-last');}
colWidth=Math.floor((slotTableWidth-axisWidth)/colCnt);setOuterWidth(dayHeadCells.slice(0,-1),colWidth);}
function resetScroll(){var d0=zeroDate();var scrollDate=cloneDate(d0);scrollDate.setHours(opt('firstHour'));var top=timePosition(d0,scrollDate)+1;function scroll(){slotScroller.scrollTop(top);}
scroll();setTimeout(scroll,0);}
function beforeHide(){savedScrollTop=slotScroller.scrollTop();}
function afterShow(){slotScroller.scrollTop(savedScrollTop);}
function dayBind(cells){cells.click(slotClick).mousedown(daySelectionMousedown);}
function slotBind(cells){cells.click(slotClick).mousedown(slotSelectionMousedown);}
function slotClick(ev){if(!opt('selectable')){var col=Math.min(colCnt-1,Math.floor((ev.pageX-dayTable.offset().left-axisWidth)/colWidth));var date=colDate(col);var rowMatch=this.parentNode.className.match(/fc-slot(\d+)/);if(rowMatch){var mins=parseInt(rowMatch[1])*opt('slotMinutes');var hours=Math.floor(mins/60);date.setHours(hours);date.setMinutes(mins%60+minMinute);trigger('dayClick',dayBodyCells[col],date,false,ev);}else{trigger('dayClick',dayBodyCells[col],date,true,ev);}}}
function renderDayOverlay(startDate,endDate,refreshCoordinateGrid){if(refreshCoordinateGrid){coordinateGrid.build();}
var visStart=cloneDate(t.visStart);var startCol,endCol;if(rtl){startCol=dayDiff(endDate,visStart)*dis+dit+1;endCol=dayDiff(startDate,visStart)*dis+dit+1;}else{startCol=dayDiff(startDate,visStart);endCol=dayDiff(endDate,visStart);}
startCol=Math.max(0,startCol);endCol=Math.min(colCnt,endCol);if(startCol<endCol){dayBind(renderCellOverlay(0,startCol,0,endCol-1));}}
function renderCellOverlay(row0,col0,row1,col1){var rect=coordinateGrid.rect(row0,col0,row1,col1,slotLayer);return renderOverlay(rect,slotLayer);}
function renderSlotOverlay(overlayStart,overlayEnd){var dayStart=cloneDate(t.visStart);var dayEnd=addDays(cloneDate(dayStart),1);for(var i=0;i<colCnt;i++){var stretchStart=new Date(Math.max(dayStart,overlayStart));var stretchEnd=new Date(Math.min(dayEnd,overlayEnd));if(stretchStart<stretchEnd){var col=i*dis+dit;var rect=coordinateGrid.rect(0,col,0,col,slotContent);var top=timePosition(dayStart,stretchStart);var bottom=timePosition(dayStart,stretchEnd);rect.top=top;rect.height=bottom-top;slotBind(renderOverlay(rect,slotContent));}
addDays(dayStart,1);addDays(dayEnd,1);}}
coordinateGrid=new CoordinateGrid(function(rows,cols){var e,n,p;dayHeadCells.each(function(i,_e){e=$(_e);n=e.offset().left;if(i){p[1]=n;}
p=[n];cols[i]=p;});p[1]=n+e.outerWidth();if(opt('allDaySlot')){e=allDayRow;n=e.offset().top;rows[0]=[n,n+e.outerHeight()];}
var slotTableTop=slotContent.offset().top;var slotScrollerTop=slotScroller.offset().top;var slotScrollerBottom=slotScrollerTop+slotScroller.outerHeight();function constrain(n){return Math.max(slotScrollerTop,Math.min(slotScrollerBottom,n));}
for(var i=0;i<slotCnt;i++){rows.push([constrain(slotTableTop+slotHeight*i),constrain(slotTableTop+slotHeight*(i+1))]);}});hoverListener=new HoverListener(coordinateGrid);colContentPositions=new HorizontalPositionCache(function(col){return dayBodyCellInners.eq(col);});function colContentLeft(col){return colContentPositions.left(col);}
function colContentRight(col){return colContentPositions.right(col);}
function dateCell(date){return{row:Math.floor(dayDiff(date,t.visStart)/7),col:dayOfWeekCol(date.getDay())};}
function cellDate(cell){var d=colDate(cell.col);var slotIndex=cell.row;if(opt('allDaySlot')){slotIndex--;}
if(slotIndex>=0){addMinutes(d,minMinute+slotIndex*opt('slotMinutes'));}
return d;}
function colDate(col){return addDays(cloneDate(t.visStart),col*dis+dit);}
function cellIsAllDay(cell){return opt('allDaySlot')&&!cell.row;}
function dayOfWeekCol(dayOfWeek){return((dayOfWeek-Math.max(firstDay,nwe)+colCnt)%colCnt)*dis+dit;}
function timePosition(day,time){day=cloneDate(day,true);if(time<addMinutes(cloneDate(day),minMinute)){return 0;}
if(time>=addMinutes(cloneDate(day),maxMinute)){return slotTable.height();}
var slotMinutes=opt('slotMinutes'),minutes=time.getHours()*60+time.getMinutes()-minMinute,slotI=Math.floor(minutes/slotMinutes),slotTop=slotTopCache[slotI];if(slotTop===undefined){slotTop=slotTopCache[slotI]=slotTable.find('tr:eq('+slotI+') td div')[0].offsetTop;}
return Math.max(0,Math.round(slotTop-1+slotHeight*((minutes%slotMinutes)/slotMinutes)));}
function allDayBounds(){return{left:axisWidth,right:viewWidth-gutterWidth}}
function getAllDayRow(index){return allDayRow;}
function defaultEventEnd(event){var start=cloneDate(event.start);if(event.allDay){return start;}
return addMinutes(start,opt('defaultEventMinutes'));}
function defaultSelectionEnd(startDate,allDay){if(allDay){return cloneDate(startDate);}
return addMinutes(cloneDate(startDate),opt('slotMinutes'));}
function renderSelection(startDate,endDate,allDay){if(allDay){if(opt('allDaySlot')){renderDayOverlay(startDate,addDays(cloneDate(endDate),1),true);}}else{renderSlotSelection(startDate,endDate);}}
function renderSlotSelection(startDate,endDate){var helperOption=opt('selectHelper');coordinateGrid.build();if(helperOption){var col=dayDiff(startDate,t.visStart)*dis+dit;if(col>=0&&col<colCnt){var rect=coordinateGrid.rect(0,col,0,col,slotContent);var top=timePosition(startDate,startDate);var bottom=timePosition(startDate,endDate);if(bottom>top){rect.top=top;rect.height=bottom-top;rect.left+=2;rect.width-=5;if($.isFunction(helperOption)){var helperRes=helperOption(startDate,endDate);if(helperRes){rect.position='absolute';rect.zIndex=8;selectionHelper=$(helperRes).css(rect).appendTo(slotContent);}}else{rect.isStart=true;rect.isEnd=true;selectionHelper=$(slotSegHtml({title:'',start:startDate,end:endDate,className:['fc-select-helper'],editable:false},rect));selectionHelper.css('opacity',opt('dragOpacity'));}
if(selectionHelper){slotBind(selectionHelper);slotContent.append(selectionHelper);setOuterWidth(selectionHelper,rect.width,true);setOuterHeight(selectionHelper,rect.height,true);}}}}else{renderSlotOverlay(startDate,endDate);}}
function clearSelection(){clearOverlays();if(selectionHelper){selectionHelper.remove();selectionHelper=null;}}
function slotSelectionMousedown(ev){if(ev.which==1&&opt('selectable')){unselect(ev);var dates;hoverListener.start(function(cell,origCell){clearSelection();if(cell&&cell.col==origCell.col&&!cellIsAllDay(cell)){var d1=cellDate(origCell);var d2=cellDate(cell);dates=[d1,addMinutes(cloneDate(d1),opt('slotMinutes')),d2,addMinutes(cloneDate(d2),opt('slotMinutes'))].sort(cmp);renderSlotSelection(dates[0],dates[3]);}else{dates=null;}},ev);$(document).one('mouseup',function(ev){hoverListener.stop();if(dates){if(+dates[0]==+dates[1]){reportDayClick(dates[0],false,ev);}
reportSelection(dates[0],dates[3],false,ev);}});}}
function reportDayClick(date,allDay,ev){trigger('dayClick',dayBodyCells[dayOfWeekCol(date.getDay())],date,allDay,ev);}
function dragStart(_dragElement,ev,ui){hoverListener.start(function(cell){clearOverlays();if(cell){if(cellIsAllDay(cell)){renderCellOverlay(cell.row,cell.col,cell.row,cell.col);}else{var d1=cellDate(cell);var d2=addMinutes(cloneDate(d1),opt('defaultEventMinutes'));renderSlotOverlay(d1,d2);}}},ev);}
function dragStop(_dragElement,ev,ui){var cell=hoverListener.stop();clearOverlays();if(cell){trigger('drop',_dragElement,cellDate(cell),cellIsAllDay(cell),ev,ui);}}}
function AgendaEventRenderer(){var t=this;t.renderEvents=renderEvents;t.compileDaySegs=compileDaySegs;t.clearEvents=clearEvents;t.slotSegHtml=slotSegHtml;t.bindDaySeg=bindDaySeg;DayEventRenderer.call(t);var opt=t.opt;var trigger=t.trigger;var isEventDraggable=t.isEventDraggable;var isEventResizable=t.isEventResizable;var eventEnd=t.eventEnd;var reportEvents=t.reportEvents;var reportEventClear=t.reportEventClear;var eventElementHandlers=t.eventElementHandlers;var setHeight=t.setHeight;var getDaySegmentContainer=t.getDaySegmentContainer;var getSlotSegmentContainer=t.getSlotSegmentContainer;var getHoverListener=t.getHoverListener;var getMaxMinute=t.getMaxMinute;var getMinMinute=t.getMinMinute;var timePosition=t.timePosition;var colContentLeft=t.colContentLeft;var colContentRight=t.colContentRight;var renderDaySegs=t.renderDaySegs;var resizableDayEvent=t.resizableDayEvent;var getColCnt=t.getColCnt;var getColWidth=t.getColWidth;var getSlotHeight=t.getSlotHeight;var getBodyContent=t.getBodyContent;var reportEventElement=t.reportEventElement;var showEvents=t.showEvents;var hideEvents=t.hideEvents;var eventDrop=t.eventDrop;var eventResize=t.eventResize;var renderDayOverlay=t.renderDayOverlay;var clearOverlays=t.clearOverlays;var calendar=t.calendar;var formatDate=calendar.formatDate;var formatDates=calendar.formatDates;function renderEvents(events,modifiedEventId){reportEvents(events);var i,len=events.length,dayEvents=[],slotEvents=[];for(i=0;i<len;i++){if(events[i].allDay){dayEvents.push(events[i]);}else{slotEvents.push(events[i]);}}
if(opt('allDaySlot')){renderDaySegs(compileDaySegs(dayEvents),modifiedEventId);setHeight();}
renderSlotSegs(compileSlotSegs(slotEvents),modifiedEventId);}
function clearEvents(){reportEventClear();getDaySegmentContainer().empty();getSlotSegmentContainer().empty();}
function compileDaySegs(events){var levels=stackSegs(sliceSegs(events,$.map(events,exclEndDay),t.visStart,t.visEnd)),i,levelCnt=levels.length,level,j,seg,segs=[];for(i=0;i<levelCnt;i++){level=levels[i];for(j=0;j<level.length;j++){seg=level[j];seg.row=0;seg.level=i;segs.push(seg);}}
return segs;}
function compileSlotSegs(events){var colCnt=getColCnt(),minMinute=getMinMinute(),maxMinute=getMaxMinute(),d=addMinutes(cloneDate(t.visStart),minMinute),visEventEnds=$.map(events,slotEventEnd),i,col,j,level,k,seg,segs=[];for(i=0;i<colCnt;i++){col=stackSegs(sliceSegs(events,visEventEnds,d,addMinutes(cloneDate(d),maxMinute-minMinute)));countForwardSegs(col);for(j=0;j<col.length;j++){level=col[j];for(k=0;k<level.length;k++){seg=level[k];seg.col=i;seg.level=j;segs.push(seg);}}
addDays(d,1,true);}
return segs;}
function slotEventEnd(event){if(event.end){return cloneDate(event.end);}else{return addMinutes(cloneDate(event.start),opt('defaultEventMinutes'));}}
function renderSlotSegs(segs,modifiedEventId){var i,segCnt=segs.length,seg,event,classes,top,bottom,colI,levelI,forward,leftmost,availWidth,outerWidth,left,html='',eventElements,eventElement,triggerRes,vsideCache={},hsideCache={},key,val,contentElement,height,slotSegmentContainer=getSlotSegmentContainer(),rtl,dis,dit,colCnt=getColCnt();if(rtl=opt('isRTL')){dis=-1;dit=colCnt-1;}else{dis=1;dit=0;}
for(i=0;i<segCnt;i++){seg=segs[i];event=seg.event;top=timePosition(seg.start,seg.start);bottom=timePosition(seg.start,seg.end);colI=seg.col;levelI=seg.level;forward=seg.forward||0;leftmost=colContentLeft(colI*dis+dit);availWidth=colContentRight(colI*dis+dit)-leftmost;availWidth=Math.min(availWidth-6,availWidth*.95);if(levelI){outerWidth=availWidth/(levelI+forward+1);}else{if(forward){outerWidth=((availWidth/(forward+1))-(12/2))*2;}else{outerWidth=availWidth;}}
left=leftmost+
(availWidth/(levelI+forward+1)*levelI)*dis+(rtl?availWidth-outerWidth:0);seg.top=top;seg.left=left;seg.outerWidth=outerWidth;seg.outerHeight=bottom-top;html+=slotSegHtml(event,seg);}
slotSegmentContainer[0].innerHTML=html;eventElements=slotSegmentContainer.children();for(i=0;i<segCnt;i++){seg=segs[i];event=seg.event;eventElement=$(eventElements[i]);triggerRes=trigger('eventRender',event,event,eventElement);if(triggerRes===false){eventElement.remove();}else{if(triggerRes&&triggerRes!==true){eventElement.remove();eventElement=$(triggerRes).css({position:'absolute',top:seg.top,left:seg.left}).appendTo(slotSegmentContainer);}
seg.element=eventElement;if(event._id===modifiedEventId){bindSlotSeg(event,eventElement,seg);}else{eventElement[0]._fci=i;}
reportEventElement(event,eventElement);}}
lazySegBind(slotSegmentContainer,segs,bindSlotSeg);for(i=0;i<segCnt;i++){seg=segs[i];if(eventElement=seg.element){val=vsideCache[key=seg.key=cssKey(eventElement[0])];seg.vsides=val===undefined?(vsideCache[key]=vsides(eventElement,true)):val;val=hsideCache[key];seg.hsides=val===undefined?(hsideCache[key]=hsides(eventElement,true)):val;contentElement=eventElement.find('div.fc-event-content');if(contentElement.length){seg.contentTop=contentElement[0].offsetTop;}}}
for(i=0;i<segCnt;i++){seg=segs[i];if(eventElement=seg.element){eventElement[0].style.width=Math.max(0,seg.outerWidth-seg.hsides)+'px';height=Math.max(0,seg.outerHeight-seg.vsides);eventElement[0].style.height=height+'px';event=seg.event;if(seg.contentTop!==undefined&&height-seg.contentTop<10){eventElement.find('div.fc-event-time').text(formatDate(event.start,opt('timeFormat'))+' - '+event.title);eventElement.find('div.fc-event-title').remove();}
trigger('eventAfterRender',event,event,eventElement);}}}
function slotSegHtml(event,seg){var html="<";var url=event.url;var skinCss=getSkinCss(event,opt);var skinCssAttr=(skinCss?" style='"+skinCss+"'":'');var classes=['fc-event','fc-event-skin','fc-event-vert'];if(isEventDraggable(event)){classes.push('fc-event-draggable');}
if(seg.isStart){classes.push('fc-corner-top');}
if(seg.isEnd){classes.push('fc-corner-bottom');}
classes=classes.concat(event.className);if(event.source){classes=classes.concat(event.source.className||[]);}
if(url){html+="a href='"+htmlEscape(event.url)+"'";}else{html+="div";}
html+=" class='"+classes.join(' ')+"'"+" style='position:absolute;z-index:8;top:"+seg.top+"px;left:"+seg.left+"px;"+skinCss+"'"+">"+"<div class='fc-event-inner fc-event-skin'"+skinCssAttr+">"+"<div class='fc-event-head fc-event-skin'"+skinCssAttr+">"+"<div class='fc-event-time'>"+
htmlEscape(formatDates(event.start,event.end,opt('timeFormat')))+"</div>"+"</div>"+"<div class='fc-event-content'>"+"<div class='fc-event-title'>"+
htmlEscape(event.title)+"</div>"+"</div>"+"<div class='fc-event-bg'></div>"+"</div>";if(seg.isEnd&&isEventResizable(event)){html+="<div class='ui-resizable-handle ui-resizable-s'>=</div>";}
html+="</"+(url?"a":"div")+">";return html;}
function bindDaySeg(event,eventElement,seg){if(isEventDraggable(event)){draggableDayEvent(event,eventElement,seg.isStart);}
if(seg.isEnd&&isEventResizable(event)){resizableDayEvent(event,eventElement,seg);}
eventElementHandlers(event,eventElement);}
function bindSlotSeg(event,eventElement,seg){var timeElement=eventElement.find('div.fc-event-time');if(isEventDraggable(event)){draggableSlotEvent(event,eventElement,timeElement);}
if(seg.isEnd&&isEventResizable(event)){resizableSlotEvent(event,eventElement,timeElement);}
eventElementHandlers(event,eventElement);}
function draggableDayEvent(event,eventElement,isStart){var origWidth;var revert;var allDay=true;var dayDelta;var dis=opt('isRTL')?-1:1;var hoverListener=getHoverListener();var colWidth=getColWidth();var slotHeight=getSlotHeight();var minMinute=getMinMinute();eventElement.draggable({zIndex:9,opacity:opt('dragOpacity','month'),revertDuration:opt('dragRevertDuration'),start:function(ev,ui){trigger('eventDragStart',eventElement,event,ev,ui);hideEvents(event,eventElement);origWidth=eventElement.width();hoverListener.start(function(cell,origCell,rowDelta,colDelta){clearOverlays();if(cell){revert=false;dayDelta=colDelta*dis;if(!cell.row){renderDayOverlay(addDays(cloneDate(event.start),dayDelta),addDays(exclEndDay(event),dayDelta));resetElement();}else{if(isStart){if(allDay){eventElement.width(colWidth-10);setOuterHeight(eventElement,slotHeight*Math.round((event.end?((event.end-event.start)/MINUTE_MS):opt('defaultEventMinutes'))/opt('slotMinutes')));eventElement.draggable('option','grid',[colWidth,1]);allDay=false;}}else{revert=true;}}
revert=revert||(allDay&&!dayDelta);}else{resetElement();revert=true;}
eventElement.draggable('option','revert',revert);},ev,'drag');},stop:function(ev,ui){hoverListener.stop();clearOverlays();trigger('eventDragStop',eventElement,event,ev,ui);if(revert){resetElement();eventElement.css('filter','');showEvents(event,eventElement);}else{var minuteDelta=0;if(!allDay){minuteDelta=Math.round((eventElement.offset().top-getBodyContent().offset().top)/slotHeight)*opt('slotMinutes')
+minMinute
-(event.start.getHours()*60+event.start.getMinutes());}
eventDrop(this,event,dayDelta,minuteDelta,allDay,ev,ui);}}});function resetElement(){if(!allDay){eventElement.width(origWidth).height('').draggable('option','grid',null);allDay=true;}}}
function draggableSlotEvent(event,eventElement,timeElement){var origPosition;var allDay=false;var dayDelta;var minuteDelta;var prevMinuteDelta;var dis=opt('isRTL')?-1:1;var hoverListener=getHoverListener();var colCnt=getColCnt();var colWidth=getColWidth();var slotHeight=getSlotHeight();eventElement.draggable({zIndex:9,scroll:false,grid:[colWidth,slotHeight],axis:colCnt==1?'y':false,opacity:opt('dragOpacity'),revertDuration:opt('dragRevertDuration'),start:function(ev,ui){trigger('eventDragStart',eventElement,event,ev,ui);hideEvents(event,eventElement);origPosition=eventElement.position();minuteDelta=prevMinuteDelta=0;hoverListener.start(function(cell,origCell,rowDelta,colDelta){eventElement.draggable('option','revert',!cell);clearOverlays();if(cell){dayDelta=colDelta*dis;if(opt('allDaySlot')&&!cell.row){if(!allDay){allDay=true;timeElement.hide();eventElement.draggable('option','grid',null);}
renderDayOverlay(addDays(cloneDate(event.start),dayDelta),addDays(exclEndDay(event),dayDelta));}else{resetElement();}}},ev,'drag');},drag:function(ev,ui){minuteDelta=Math.round((ui.position.top-origPosition.top)/slotHeight)*opt('slotMinutes');if(minuteDelta!=prevMinuteDelta){if(!allDay){updateTimeText(minuteDelta);}
prevMinuteDelta=minuteDelta;}},stop:function(ev,ui){var cell=hoverListener.stop();clearOverlays();trigger('eventDragStop',eventElement,event,ev,ui);if(cell&&(dayDelta||minuteDelta||allDay)){eventDrop(this,event,dayDelta,allDay?0:minuteDelta,allDay,ev,ui);}else{resetElement();eventElement.css('filter','');eventElement.css(origPosition);updateTimeText(0);showEvents(event,eventElement);}}});function updateTimeText(minuteDelta){var newStart=addMinutes(cloneDate(event.start),minuteDelta);var newEnd;if(event.end){newEnd=addMinutes(cloneDate(event.end),minuteDelta);}
timeElement.text(formatDates(newStart,newEnd,opt('timeFormat')));}
function resetElement(){if(allDay){timeElement.css('display','');eventElement.draggable('option','grid',[colWidth,slotHeight]);allDay=false;}}}
function resizableSlotEvent(event,eventElement,timeElement){var slotDelta,prevSlotDelta;var slotHeight=getSlotHeight();eventElement.resizable({handles:{s:'div.ui-resizable-s'},grid:slotHeight,start:function(ev,ui){slotDelta=prevSlotDelta=0;hideEvents(event,eventElement);eventElement.css('z-index',9);trigger('eventResizeStart',this,event,ev,ui);},resize:function(ev,ui){slotDelta=Math.round((Math.max(slotHeight,eventElement.height())-ui.originalSize.height)/slotHeight);if(slotDelta!=prevSlotDelta){timeElement.text(formatDates(event.start,(!slotDelta&&!event.end)?null:addMinutes(eventEnd(event),opt('slotMinutes')*slotDelta),opt('timeFormat')));prevSlotDelta=slotDelta;}},stop:function(ev,ui){trigger('eventResizeStop',this,event,ev,ui);if(slotDelta){eventResize(this,event,0,opt('slotMinutes')*slotDelta,ev,ui);}else{eventElement.css('z-index',8);showEvents(event,eventElement);}}});}}
function countForwardSegs(levels){var i,j,k,level,segForward,segBack;for(i=levels.length-1;i>0;i--){level=levels[i];for(j=0;j<level.length;j++){segForward=level[j];for(k=0;k<levels[i-1].length;k++){segBack=levels[i-1][k];if(segsCollide(segForward,segBack)){segBack.forward=Math.max(segBack.forward||0,(segForward.forward||0)+1);}}}}}
function View(element,calendar,viewName){var t=this;t.element=element;t.calendar=calendar;t.name=viewName;t.opt=opt;t.trigger=trigger;t.isEventDraggable=isEventDraggable;t.isEventResizable=isEventResizable;t.reportEvents=reportEvents;t.eventEnd=eventEnd;t.reportEventElement=reportEventElement;t.reportEventClear=reportEventClear;t.eventElementHandlers=eventElementHandlers;t.showEvents=showEvents;t.hideEvents=hideEvents;t.eventDrop=eventDrop;t.eventResize=eventResize;var defaultEventEnd=t.defaultEventEnd;var normalizeEvent=calendar.normalizeEvent;var reportEventChange=calendar.reportEventChange;var eventsByID={};var eventElements=[];var eventElementsByID={};var options=calendar.options;function opt(name,viewNameOverride){var v=options[name];if(typeof v=='object'){return smartProperty(v,viewNameOverride||viewName);}
return v;}
function trigger(name,thisObj){return calendar.trigger.apply(calendar,[name,thisObj||t].concat(Array.prototype.slice.call(arguments,2),[t]));}
function isEventDraggable(event){return isEventEditable(event)&&!opt('disableDragging');}
function isEventResizable(event){return isEventEditable(event)&&!opt('disableResizing');}
function isEventEditable(event){return firstDefined(event.editable,(event.source||{}).editable,opt('editable'));}
function reportEvents(events){eventsByID={};var i,len=events.length,event;for(i=0;i<len;i++){event=events[i];if(eventsByID[event._id]){eventsByID[event._id].push(event);}else{eventsByID[event._id]=[event];}}}
function eventEnd(event){return event.end?cloneDate(event.end):defaultEventEnd(event);}
function reportEventElement(event,element){eventElements.push(element);if(eventElementsByID[event._id]){eventElementsByID[event._id].push(element);}else{eventElementsByID[event._id]=[element];}}
function reportEventClear(){eventElements=[];eventElementsByID={};}
function eventElementHandlers(event,eventElement){eventElement.click(function(ev){if(!eventElement.hasClass('ui-draggable-dragging')&&!eventElement.hasClass('ui-resizable-resizing')){return trigger('eventClick',this,event,ev);}}).hover(function(ev){trigger('eventMouseover',this,event,ev);},function(ev){trigger('eventMouseout',this,event,ev);});}
function showEvents(event,exceptElement){eachEventElement(event,exceptElement,'show');}
function hideEvents(event,exceptElement){eachEventElement(event,exceptElement,'hide');}
function eachEventElement(event,exceptElement,funcName){var elements=eventElementsByID[event._id],i,len=elements.length;for(i=0;i<len;i++){if(!exceptElement||elements[i][0]!=exceptElement[0]){elements[i][funcName]();}}}
function eventDrop(e,event,dayDelta,minuteDelta,allDay,ev,ui){var oldAllDay=event.allDay;var eventId=event._id;moveEvents(eventsByID[eventId],dayDelta,minuteDelta,allDay);trigger('eventDrop',e,event,dayDelta,minuteDelta,allDay,function(){moveEvents(eventsByID[eventId],-dayDelta,-minuteDelta,oldAllDay);reportEventChange(eventId);},ev,ui);reportEventChange(eventId);}
function eventResize(e,event,dayDelta,minuteDelta,ev,ui){var eventId=event._id;elongateEvents(eventsByID[eventId],dayDelta,minuteDelta);trigger('eventResize',e,event,dayDelta,minuteDelta,function(){elongateEvents(eventsByID[eventId],-dayDelta,-minuteDelta);reportEventChange(eventId);},ev,ui);reportEventChange(eventId);}
function moveEvents(events,dayDelta,minuteDelta,allDay){minuteDelta=minuteDelta||0;for(var e,len=events.length,i=0;i<len;i++){e=events[i];if(allDay!==undefined){e.allDay=allDay;}
addMinutes(addDays(e.start,dayDelta,true),minuteDelta);if(e.end){e.end=addMinutes(addDays(e.end,dayDelta,true),minuteDelta);}
normalizeEvent(e,options);}}
function elongateEvents(events,dayDelta,minuteDelta){minuteDelta=minuteDelta||0;for(var e,len=events.length,i=0;i<len;i++){e=events[i];e.end=addMinutes(addDays(eventEnd(e),dayDelta,true),minuteDelta);normalizeEvent(e,options);}}}
function DayEventRenderer(){var t=this;t.renderDaySegs=renderDaySegs;t.resizableDayEvent=resizableDayEvent;var opt=t.opt;var trigger=t.trigger;var isEventDraggable=t.isEventDraggable;var isEventResizable=t.isEventResizable;var eventEnd=t.eventEnd;var reportEventElement=t.reportEventElement;var showEvents=t.showEvents;var hideEvents=t.hideEvents;var eventResize=t.eventResize;var getRowCnt=t.getRowCnt;var getColCnt=t.getColCnt;var getColWidth=t.getColWidth;var allDayRow=t.allDayRow;var allDayBounds=t.allDayBounds;var colContentLeft=t.colContentLeft;var colContentRight=t.colContentRight;var dayOfWeekCol=t.dayOfWeekCol;var dateCell=t.dateCell;var compileDaySegs=t.compileDaySegs;var getDaySegmentContainer=t.getDaySegmentContainer;var bindDaySeg=t.bindDaySeg;var formatDates=t.calendar.formatDates;var renderDayOverlay=t.renderDayOverlay;var clearOverlays=t.clearOverlays;var clearSelection=t.clearSelection;function renderDaySegs(segs,modifiedEventId){var segmentContainer=getDaySegmentContainer();var rowDivs;var rowCnt=getRowCnt();var colCnt=getColCnt();var i=0;var rowI;var levelI;var colHeights;var j;var segCnt=segs.length;var seg;var top;var k;segmentContainer[0].innerHTML=daySegHTML(segs);daySegElementResolve(segs,segmentContainer.children());daySegElementReport(segs);daySegHandlers(segs,segmentContainer,modifiedEventId);daySegCalcHSides(segs);daySegSetWidths(segs);daySegCalcHeights(segs);rowDivs=getRowDivs();for(rowI=0;rowI<rowCnt;rowI++){levelI=0;colHeights=[];for(j=0;j<colCnt;j++){colHeights[j]=0;}
while(i<segCnt&&(seg=segs[i]).row==rowI){top=arrayMax(colHeights.slice(seg.startCol,seg.endCol));seg.top=top;top+=seg.outerHeight;for(k=seg.startCol;k<seg.endCol;k++){colHeights[k]=top;}
i++;}
rowDivs[rowI].height(arrayMax(colHeights));}
daySegSetTops(segs,getRowTops(rowDivs));}
function renderTempDaySegs(segs,adjustRow,adjustTop){var tempContainer=$("<div/>");var elements;var segmentContainer=getDaySegmentContainer();var i;var segCnt=segs.length;var element;tempContainer[0].innerHTML=daySegHTML(segs);elements=tempContainer.children();segmentContainer.append(elements);daySegElementResolve(segs,elements);daySegCalcHSides(segs);daySegSetWidths(segs);daySegCalcHeights(segs);daySegSetTops(segs,getRowTops(getRowDivs()));elements=[];for(i=0;i<segCnt;i++){element=segs[i].element;if(element){if(segs[i].row===adjustRow){element.css('top',adjustTop);}
elements.push(element[0]);}}
return $(elements);}
function daySegHTML(segs){var rtl=opt('isRTL');var i;var segCnt=segs.length;var seg;var event;var url;var classes;var bounds=allDayBounds();var minLeft=bounds.left;var maxLeft=bounds.right;var leftCol;var rightCol;var left;var right;var skinCss;var html='';for(i=0;i<segCnt;i++){seg=segs[i];event=seg.event;classes=['fc-event','fc-event-skin','fc-event-hori'];if(isEventDraggable(event)){classes.push('fc-event-draggable');}
if(rtl){if(seg.isStart){classes.push('fc-corner-right');}
if(seg.isEnd){classes.push('fc-corner-left');}
leftCol=dayOfWeekCol(seg.end.getDay()-1);rightCol=dayOfWeekCol(seg.start.getDay());left=seg.isEnd?colContentLeft(leftCol):minLeft;right=seg.isStart?colContentRight(rightCol):maxLeft;}else{if(seg.isStart){classes.push('fc-corner-left');}
if(seg.isEnd){classes.push('fc-corner-right');}
leftCol=dayOfWeekCol(seg.start.getDay());rightCol=dayOfWeekCol(seg.end.getDay()-1);left=seg.isStart?colContentLeft(leftCol):minLeft;right=seg.isEnd?colContentRight(rightCol):maxLeft;}
classes=classes.concat(event.className);if(event.source){classes=classes.concat(event.source.className||[]);}
url=event.url;skinCss=getSkinCss(event,opt);if(url){html+="<a href='"+htmlEscape(url)+"'";}else{html+="<div";}
html+=" class='"+classes.join(' ')+"'"+" style='position:absolute;z-index:8;left:"+left+"px;"+skinCss+"'"+">"+"<div"+" class='fc-event-inner fc-event-skin'"+
(skinCss?" style='"+skinCss+"'":'')+">";if(!event.allDay&&seg.isStart){html+="<span class='fc-event-time'>"+
htmlEscape(formatDates(event.start,event.end,opt('timeFormat')))+"</span>";}
html+="<span class='fc-event-title'>"+htmlEscape(event.title)+"</span>"+"</div>";if(seg.isEnd&&isEventResizable(event)){html+="<div class='ui-resizable-handle ui-resizable-"+(rtl?'w':'e')+"'>"+"&nbsp;&nbsp;&nbsp;"+"</div>";}
html+="</"+(url?"a":"div")+">";seg.left=left;seg.outerWidth=right-left;seg.startCol=leftCol;seg.endCol=rightCol+1;}
return html;}
function daySegElementResolve(segs,elements){var i;var segCnt=segs.length;var seg;var event;var element;var triggerRes;for(i=0;i<segCnt;i++){seg=segs[i];event=seg.event;element=$(elements[i]);triggerRes=trigger('eventRender',event,event,element);if(triggerRes===false){element.remove();}else{if(triggerRes&&triggerRes!==true){triggerRes=$(triggerRes).css({position:'absolute',left:seg.left});element.replaceWith(triggerRes);element=triggerRes;}
seg.element=element;}}}
function daySegElementReport(segs){var i;var segCnt=segs.length;var seg;var element;for(i=0;i<segCnt;i++){seg=segs[i];element=seg.element;if(element){reportEventElement(seg.event,element);}}}
function daySegHandlers(segs,segmentContainer,modifiedEventId){var i;var segCnt=segs.length;var seg;var element;var event;for(i=0;i<segCnt;i++){seg=segs[i];element=seg.element;if(element){event=seg.event;if(event._id===modifiedEventId){bindDaySeg(event,element,seg);}else{element[0]._fci=i;}}}
lazySegBind(segmentContainer,segs,bindDaySeg);}
function daySegCalcHSides(segs){var i;var segCnt=segs.length;var seg;var element;var key,val;var hsideCache={};for(i=0;i<segCnt;i++){seg=segs[i];element=seg.element;if(element){key=seg.key=cssKey(element[0]);val=hsideCache[key];if(val===undefined){val=hsideCache[key]=hsides(element,true);}
seg.hsides=val;}}}
function daySegSetWidths(segs){var i;var segCnt=segs.length;var seg;var element;for(i=0;i<segCnt;i++){seg=segs[i];element=seg.element;if(element){element[0].style.width=Math.max(0,seg.outerWidth-seg.hsides)+'px';}}}
function daySegCalcHeights(segs){var i;var segCnt=segs.length;var seg;var element;var key,val;var vmarginCache={};for(i=0;i<segCnt;i++){seg=segs[i];element=seg.element;if(element){key=seg.key;val=vmarginCache[key];if(val===undefined){val=vmarginCache[key]=vmargins(element);}
seg.outerHeight=element[0].offsetHeight+val;}}}
function getRowDivs(){var i;var rowCnt=getRowCnt();var rowDivs=[];for(i=0;i<rowCnt;i++){rowDivs[i]=allDayRow(i).find('td:first div.fc-day-content > div');}
return rowDivs;}
function getRowTops(rowDivs){var i;var rowCnt=rowDivs.length;var tops=[];for(i=0;i<rowCnt;i++){tops[i]=rowDivs[i][0].offsetTop;}
return tops;}
function daySegSetTops(segs,rowTops){var i;var segCnt=segs.length;var seg;var element;var event;for(i=0;i<segCnt;i++){seg=segs[i];element=seg.element;if(element){element[0].style.top=rowTops[seg.row]+(seg.top||0)+'px';event=seg.event;trigger('eventAfterRender',event,event,element);}}}
function resizableDayEvent(event,element,seg){var rtl=opt('isRTL');var direction=rtl?'w':'e';var handle=element.find('div.ui-resizable-'+direction);var isResizing=false;disableTextSelection(element);element.mousedown(function(ev){ev.preventDefault();}).click(function(ev){if(isResizing){ev.preventDefault();ev.stopImmediatePropagation();}});handle.mousedown(function(ev){if(ev.which!=1){return;}
isResizing=true;var hoverListener=t.getHoverListener();var rowCnt=getRowCnt();var colCnt=getColCnt();var dis=rtl?-1:1;var dit=rtl?colCnt-1:0;var elementTop=element.css('top');var dayDelta;var helpers;var eventCopy=$.extend({},event);var minCell=dateCell(event.start);clearSelection();$('body').css('cursor',direction+'-resize').one('mouseup',mouseup);trigger('eventResizeStart',this,event,ev);hoverListener.start(function(cell,origCell){if(cell){var r=Math.max(minCell.row,cell.row);var c=cell.col;if(rowCnt==1){r=0;}
if(r==minCell.row){if(rtl){c=Math.min(minCell.col,c);}else{c=Math.max(minCell.col,c);}}
dayDelta=(r*7+c*dis+dit)-(origCell.row*7+origCell.col*dis+dit);var newEnd=addDays(eventEnd(event),dayDelta,true);if(dayDelta){eventCopy.end=newEnd;var oldHelpers=helpers;helpers=renderTempDaySegs(compileDaySegs([eventCopy]),seg.row,elementTop);helpers.find('*').css('cursor',direction+'-resize');if(oldHelpers){oldHelpers.remove();}
hideEvents(event);}else{if(helpers){showEvents(event);helpers.remove();helpers=null;}}
clearOverlays();renderDayOverlay(event.start,addDays(cloneDate(newEnd),1));}},ev);function mouseup(ev){trigger('eventResizeStop',this,event,ev);$('body').css('cursor','');hoverListener.stop();clearOverlays();if(dayDelta){eventResize(this,event,dayDelta,0,ev);}
setTimeout(function(){isResizing=false;},0);}});}}
function SelectionManager(){var t=this;t.select=select;t.unselect=unselect;t.reportSelection=reportSelection;t.daySelectionMousedown=daySelectionMousedown;var opt=t.opt;var trigger=t.trigger;var defaultSelectionEnd=t.defaultSelectionEnd;var renderSelection=t.renderSelection;var clearSelection=t.clearSelection;var selected=false;if(opt('selectable')&&opt('unselectAuto')){$(document).mousedown(function(ev){var ignore=opt('unselectCancel');if(ignore){if($(ev.target).parents(ignore).length){return;}}
unselect(ev);});}
function select(startDate,endDate,allDay){unselect();if(!endDate){endDate=defaultSelectionEnd(startDate,allDay);}
renderSelection(startDate,endDate,allDay);reportSelection(startDate,endDate,allDay);}
function unselect(ev){if(selected){selected=false;clearSelection();trigger('unselect',null,ev);}}
function reportSelection(startDate,endDate,allDay,ev){selected=true;trigger('select',null,startDate,endDate,allDay,ev);}
function daySelectionMousedown(ev){var cellDate=t.cellDate;var cellIsAllDay=t.cellIsAllDay;var hoverListener=t.getHoverListener();var reportDayClick=t.reportDayClick;if(ev.which==1&&opt('selectable')){unselect(ev);var _mousedownElement=this;var dates;hoverListener.start(function(cell,origCell){clearSelection();if(cell&&cellIsAllDay(cell)){dates=[cellDate(origCell),cellDate(cell)].sort(cmp);renderSelection(dates[0],dates[1],true);}else{dates=null;}},ev);$(document).one('mouseup',function(ev){hoverListener.stop();if(dates){if(+dates[0]==+dates[1]){reportDayClick(dates[0],true,ev);}
reportSelection(dates[0],dates[1],true,ev);}});}}}
function OverlayManager(){var t=this;t.renderOverlay=renderOverlay;t.clearOverlays=clearOverlays;var usedOverlays=[];var unusedOverlays=[];function renderOverlay(rect,parent){var e=unusedOverlays.shift();if(!e){e=$("<div class='fc-cell-overlay' style='position:absolute;z-index:3'/>");}
if(e[0].parentNode!=parent[0]){e.appendTo(parent);}
usedOverlays.push(e.css(rect).show());return e;}
function clearOverlays(){var e;while(e=usedOverlays.shift()){unusedOverlays.push(e.hide().unbind());}}}
function CoordinateGrid(buildFunc){var t=this;var rows;var cols;t.build=function(){rows=[];cols=[];buildFunc(rows,cols);};t.cell=function(x,y){var rowCnt=rows.length;var colCnt=cols.length;var i,r=-1,c=-1;for(i=0;i<rowCnt;i++){if(y>=rows[i][0]&&y<rows[i][1]){r=i;break;}}
for(i=0;i<colCnt;i++){if(x>=cols[i][0]&&x<cols[i][1]){c=i;break;}}
return(r>=0&&c>=0)?{row:r,col:c}:null;};t.rect=function(row0,col0,row1,col1,originElement){var origin=originElement.offset();return{top:rows[row0][0]-origin.top,left:cols[col0][0]-origin.left,width:cols[col1][1]-cols[col0][0],height:rows[row1][1]-rows[row0][0]};};}
function HoverListener(coordinateGrid){var t=this;var bindType;var change;var firstCell;var cell;t.start=function(_change,ev,_bindType){change=_change;firstCell=cell=null;coordinateGrid.build();mouse(ev);bindType=_bindType||'mousemove';$(document).bind(bindType,mouse);};function mouse(ev){_fixUIEvent(ev);var newCell=coordinateGrid.cell(ev.pageX,ev.pageY);if(!newCell!=!cell||newCell&&(newCell.row!=cell.row||newCell.col!=cell.col)){if(newCell){if(!firstCell){firstCell=newCell;}
change(newCell,firstCell,newCell.row-firstCell.row,newCell.col-firstCell.col);}else{change(newCell,firstCell);}
cell=newCell;}}
t.stop=function(){$(document).unbind(bindType,mouse);return cell;};}
function _fixUIEvent(event){if(event.pageX===undefined){event.pageX=event.originalEvent.pageX;event.pageY=event.originalEvent.pageY;}}
function HorizontalPositionCache(getElement){var t=this,elements={},lefts={},rights={};function e(i){return elements[i]=elements[i]||getElement(i);}
t.left=function(i){return lefts[i]=lefts[i]===undefined?e(i).position().left:lefts[i];};t.right=function(i){return rights[i]=rights[i]===undefined?t.left(i)+e(i).width():rights[i];};t.clear=function(){elements={};lefts={};rights={};};}})(jQuery);var Dajax={process:function(data)
{$.each(data,function(i,elem){switch(elem.cmd)
{case'alert':alert(elem.val);break;case'data':eval(elem.fun+"(elem.val);");break;case'as':if(elem.prop=='innerHTML'){$(elem.id).html(elem.val);}
else{jQuery.each($(elem.id),function(){this[elem.prop]=elem.val;});}
break;case'addcc':jQuery.each(elem.val,function(){$(elem.id).addClass(String(this));});break;case'remcc':jQuery.each(elem.val,function(){$(elem.id).removeClass(String(this));});break;case'ap':jQuery.each($(elem.id),function(){this[elem.prop]+=elem.val;});break;case'pp':jQuery.each($(elem.id),function(){this[elem.prop]=elem.val+this[elem.prop];});break;case'clr':jQuery.each($(elem.id),function(){this[elem.prop]="";});break;case'red':window.setTimeout('window.location="'+elem.url+'";',elem.delay);break;case'js':eval(elem.val);break;case'rm':$(elem.id).remove();break;default:break;}});}};(function($){"use strict";var k={},max=Math.max,min=Math.min;k.c={};k.c.d=$(document);k.c.t=function(e){return e.originalEvent.touches.length-1;};k.o=function(){var s=this;this.o=null;this.$=null;this.i=null;this.g=null;this.v=null;this.cv=null;this.x=0;this.y=0;this.$c=null;this.c=null;this.t=0;this.isInit=false;this.fgColor=null;this.pColor=null;this.dH=null;this.cH=null;this.eH=null;this.rH=null;this.run=function(){var cf=function(e,conf){var k;for(k in conf){s.o[k]=conf[k];}
s.init();s._configure()._draw();};if(this.$.data('kontroled'))return;this.$.data('kontroled',true);this.extend();this.o=$.extend({min:this.$.data('min')||0,max:this.$.data('max')||100,stopper:true,readOnly:this.$.data('readonly'),cursor:(this.$.data('cursor')===true&&30)||this.$.data('cursor')||0,thickness:this.$.data('thickness')||0.35,width:this.$.data('width')||200,height:this.$.data('height')||200,displayInput:this.$.data('displayinput')==null||this.$.data('displayinput'),displayPrevious:this.$.data('displayprevious'),fgColor:this.$.data('fgcolor')||'#87CEEB',inline:false,draw:null,change:null,cancel:null,release:null},this.o);if(this.$.is('fieldset')){this.v={};this.i=this.$.find('input')
this.i.each(function(k){var $this=$(this);s.i[k]=$this;s.v[k]=$this.val();$this.bind('change',function(){var val={};val[k]=$this.val();s.val(val);});});this.$.find('legend').remove();}else{this.i=this.$;this.v=this.$.val();(this.v=='')&&(this.v=this.o.min);this.$.bind('change',function(){s.val(s.$.val());});}
(!this.o.displayInput)&&this.$.hide();this.$c=$('<canvas width="'+
this.o.width+'px" height="'+
this.o.height+'px"></canvas>');this.c=this.$c[0].getContext("2d");this.$.wrap($('<div style="'+(this.o.inline?'display:inline;':'')+'width:'+this.o.width+'px;height:'+
this.o.height+'px;"></div>')).before(this.$c);if(this.v instanceof Object){this.cv={};this.copy(this.v,this.cv);}else{this.cv=this.v;}
this.$.bind("configure",cf).parent().bind("configure",cf);this._listen()._configure()._xy().init();this.isInit=true;this._draw();return this;};this._draw=function(){var d=true,c=document.createElement('canvas');c.width=s.o.width;c.height=s.o.height;s.g=c.getContext('2d');s.clear();s.dH&&(d=s.dH());(d!==false)&&s.draw();s.c.drawImage(c,0,0);c=null;};this._touch=function(e){var touchMove=function(e){var v=s.xy2val(e.originalEvent.touches[s.t].pageX,e.originalEvent.touches[s.t].pageY);if(v==s.cv)return;if(s.cH&&(s.cH(v)===false))return;s.change(v);s._draw();};this.t=k.c.t(e);touchMove(e);k.c.d.bind("touchmove.k",touchMove).bind("touchend.k",function(){k.c.d.unbind('touchmove.k touchend.k');if(s.rH&&(s.rH(s.cv)===false))return;s.val(s.cv);});return this;};this._mouse=function(e){var mouseMove=function(e){var v=s.xy2val(e.pageX,e.pageY);if(v==s.cv)return;if(s.cH&&(s.cH(v)===false))return;s.change(v);s._draw();};mouseMove(e);k.c.d.bind("mousemove.k",mouseMove).bind("keyup.k",function(e){if(e.keyCode===27){k.c.d.unbind("mouseup.k mousemove.k keyup.k");if(s.eH&&(s.eH()===false))return;s.cancel();}}).bind("mouseup.k",function(e){k.c.d.unbind('mousemove.k mouseup.k keyup.k');if(s.rH&&(s.rH(s.cv)===false))return;s.val(s.cv);});return this;};this._xy=function(){var o=this.$c.offset();this.x=o.left;this.y=o.top;return this;};this._listen=function(){if(!this.o.readOnly){this.$c.bind("mousedown",function(e){e.preventDefault();s._xy()._mouse(e);}).bind("touchstart",function(e){e.preventDefault();s._xy()._touch(e);});this.listen();}else{this.$.attr('readonly','readonly');}
return this;};this._configure=function(){if(this.o.draw)this.dH=this.o.draw;if(this.o.change)this.cH=this.o.change;if(this.o.cancel)this.eH=this.o.cancel;if(this.o.release)this.rH=this.o.release;if(this.o.displayPrevious){this.pColor=this.h2rgba(this.o.fgColor,"0.4");this.fgColor=this.h2rgba(this.o.fgColor,"0.6");}else{this.fgColor=this.o.fgColor;}
return this;};this._clear=function(){this.$c[0].width=this.$c[0].width;};this.listen=function(){};this.extend=function(){};this.init=function(){};this.change=function(v){};this.val=function(v){};this.xy2val=function(x,y){};this.draw=function(){};this.clear=function(){this._clear();};this.h2rgba=function(h,a){var rgb;h=h.substring(1,7)
rgb=[parseInt(h.substring(0,2),16),parseInt(h.substring(2,4),16),parseInt(h.substring(4,6),16)];return"rgba("+rgb[0]+","+rgb[1]+","+rgb[2]+","+a+")";};this.copy=function(f,t){for(var i in f){t[i]=f[i];}};};k.Dial=function(){k.o.call(this);this.startAngle=null;this.xy=null;this.radius=null;this.lineWidth=null;this.cursorExt=null;this.w2=null;this.PI2=2*Math.PI;this.extend=function(){this.o=$.extend({bgColor:this.$.data('bgcolor')||'#EEEEEE',angleOffset:this.$.data('angleoffset')||0,angleArc:this.$.data('anglearc')||360,inline:true},this.o);};this.val=function(v){if(null!=v){this.cv=this.o.stopper?max(min(v,this.o.max),this.o.min):v;this.v=this.cv;this.$.val(this.v);this._draw();}else{return this.v;}};this.xy2val=function(x,y){var a,ret;a=Math.atan2(x-(this.x+this.w2),-(y-this.y-this.w2))-this.angleOffset;if(this.angleArc!=this.PI2&&(a<0)&&(a>-0.5)){a=0;}else if(a<0){a+=this.PI2;}
ret=~~(0.5+(a*(this.o.max-this.o.min)/this.angleArc))
+this.o.min;this.o.stopper&&(ret=max(min(ret,this.o.max),this.o.min));return ret;};this.listen=function(){var s=this,mw=function(e){e.preventDefault();var ori=e.originalEvent,deltaX=ori.detail||ori.wheelDeltaX,deltaY=ori.detail||ori.wheelDeltaY,v=parseInt(s.$.val())+(deltaX>0||deltaY>0?1:deltaX<0||deltaY<0?-1:0);if(s.cH&&(s.cH(v)===false))return;s.val(v);},kval,to,m=1,kv={37:-1,38:1,39:1,40:-1};this.$.bind("keydown",function(e){var kc=e.keyCode;if(kc>=96&&kc<=105){kc=e.keyCode=kc-48;}
kval=parseInt(String.fromCharCode(kc));if(isNaN(kval)){(kc!==13)&&(kc!==8)&&(kc!==9)&&(kc!==189)&&e.preventDefault();if($.inArray(kc,[37,38,39,40])>-1){e.preventDefault();var v=parseInt(s.$.val())+kv[kc]*m;s.o.stopper&&(v=max(min(v,s.o.max),s.o.min));s.change(v);s._draw();to=window.setTimeout(function(){m*=2;},30);}}}).bind("keyup",function(e){if(isNaN(kval)){if(to){window.clearTimeout(to);to=null;m=1;s.val(s.$.val());}}else{(s.$.val()>s.o.max&&s.$.val(s.o.max))||(s.$.val()<s.o.min&&s.$.val(s.o.min));}});this.$c.bind("mousewheel DOMMouseScroll",mw);this.$.bind("mousewheel DOMMouseScroll",mw)};this.init=function(){if(this.v<this.o.min||this.v>this.o.max)this.v=this.o.min;this.$.val(this.v);this.w2=this.o.width/2;this.cursorExt=this.o.cursor/100;this.xy=this.w2;this.lineWidth=this.xy*this.o.thickness;this.radius=this.xy-this.lineWidth/2;this.o.angleOffset&&(this.o.angleOffset=isNaN(this.o.angleOffset)?0:this.o.angleOffset);this.o.angleArc&&(this.o.angleArc=isNaN(this.o.angleArc)?this.PI2:this.o.angleArc);this.angleOffset=this.o.angleOffset*Math.PI/180;this.angleArc=this.o.angleArc*Math.PI/180;this.startAngle=1.5*Math.PI+this.angleOffset;this.endAngle=1.5*Math.PI+this.angleOffset+this.angleArc;var s=max(String(Math.abs(this.o.max)).length,String(Math.abs(this.o.min)).length,2)+2;this.o.displayInput&&this.i.css({'width':((this.o.width/2+4)>>0)+'px','height':((this.o.width/3)>>0)+'px','position':'absolute','vertical-align':'middle','margin-top':((this.o.width/3)>>0)+'px','margin-left':'-'+((this.o.width*3/4+2)>>0)+'px','border':0,'background':'none','font':'bold '+((this.o.width/s)>>0)+'px Arial','text-align':'center','color':this.o.fgColor,'padding':'0px','-webkit-appearance':'none'})||this.i.css({'width':'0px','visibility':'hidden'});};this.change=function(v){this.cv=v;this.$.val(v);};this.angle=function(v){return(v-this.o.min)*this.angleArc/(this.o.max-this.o.min);};this.draw=function(){var c=this.g,a=this.angle(this.cv),sat=this.startAngle,eat=sat+a,sa,ea,r=1;c.lineWidth=this.lineWidth;this.o.cursor&&(sat=eat-this.cursorExt)&&(eat=eat+this.cursorExt);c.beginPath();c.strokeStyle=this.o.bgColor;c.arc(this.xy,this.xy,this.radius,this.endAngle,this.startAngle,true);c.stroke();if(this.o.displayPrevious){ea=this.startAngle+this.angle(this.v);sa=this.startAngle;this.o.cursor&&(sa=ea-this.cursorExt)&&(ea=ea+this.cursorExt);c.beginPath();c.strokeStyle=this.pColor;c.arc(this.xy,this.xy,this.radius,sa,ea,false);c.stroke();r=(this.cv==this.v);}
c.beginPath();c.strokeStyle=r?this.o.fgColor:this.fgColor;c.arc(this.xy,this.xy,this.radius,sat,eat,false);c.stroke();};this.cancel=function(){this.val(this.v);};};$.fn.dial=$.fn.knob=function(o){return this.each(function(){var d=new k.Dial();d.o=o;d.$=$(this);d.run();}).parent();};})(jQuery);(function($,document,Math,devicePixelRatio){var canvasSupported=document.createElement("canvas").getContext
var peity=$.fn.peity=function(type,options){if(canvasSupported){this.each(function(){var defaults=peity.defaults[type]
var data={}
var $this=$(this)
$.each($this.data(),function(name,value){if(name in defaults)data[name]=value})
var opts=$.extend({},defaults,data,options)
var chart=new Peity($this,type,opts)
chart.draw()
$this.change(function(){chart.draw()})});}
return this;};var Peity=function($elem,type,opts){this.$elem=$elem
this.type=type
this.opts=opts}
var PeityPrototype=Peity.prototype
PeityPrototype.colours=function(){var colours=this.opts.colours
var func=colours
if(!$.isFunction(func)){func=function(_,i){return colours[i%colours.length]}}
return func}
PeityPrototype.draw=function(){peity.graphers[this.type].call(this,this.opts)}
PeityPrototype.prepareCanvas=function(width,height){var canvas=this.canvas
if(canvas){this.context.clearRect(0,0,canvas.width,canvas.height)}else{canvas=$("<canvas>").attr({height:height*devicePixelRatio,width:width*devicePixelRatio})
if(devicePixelRatio!=1){canvas.css({height:height,width:width})}
this.canvas=canvas=canvas[0]
this.context=canvas.getContext("2d")
this.$elem.hide().before(canvas)}
return canvas}
PeityPrototype.values=function(){return $.map(this.$elem.text().split(this.opts.delimiter),function(value){return parseFloat(value)})}
peity.defaults={}
peity.graphers={}
peity.register=function(type,defaults,grapher){this.defaults[type]=defaults
this.graphers[type]=grapher}
peity.register('pie',{colours:["#ff9900","#fff4dd","#ffc66e"],delimiter:null,diameter:16},function(opts){if(!opts.delimiter){var delimiter=this.$elem.text().match(/[^0-9\.]/)
opts.delimiter=delimiter?delimiter[0]:","}
var values=this.values()
if(opts.delimiter=="/"){var v1=values[0]
var v2=values[1]
values=[v1,v2-v1]}
var i=0
var length=values.length
var sum=0
for(;i<length;i++){sum+=values[i]}
var canvas=this.prepareCanvas(opts.diameter,opts.diameter)
var context=this.context
var half=canvas.width/2
var pi=Math.PI
var colours=this.colours()
context.save()
context.translate(half,half)
context.rotate(-pi/2)
for(i=0;i<length;i++){var value=values[i]
var slice=(value/sum)*pi*2
context.beginPath()
context.moveTo(0,0)
context.arc(0,0,half,0,slice,false)
context.fillStyle=colours.call(this,value,i,values)
context.fill()
context.rotate(slice)}
context.restore()})
peity.register("line",{colour:"#c6d9fd",strokeColour:"#4d89f9",strokeWidth:1,delimiter:",",height:16,max:null,min:0,width:32},function(opts){var values=this.values()
if(values.length==1)values.push(values[0])
var max=Math.max.apply(Math,values.concat([opts.max]));var min=Math.min.apply(Math,values.concat([opts.min]))
var canvas=this.prepareCanvas(opts.width,opts.height)
var context=this.context
var width=canvas.width
var height=canvas.height
var xQuotient=width/(values.length-1)
var yQuotient=height/(max-min)
var coords=[];var i;context.beginPath();context.moveTo(0,height+(min*yQuotient))
for(i=0;i<values.length;i++){var x=i*xQuotient
var y=height-(yQuotient*(values[i]-min))
coords.push({x:x,y:y});context.lineTo(x,y);}
context.lineTo(width,height+(min*yQuotient))
context.fillStyle=opts.colour;context.fill();if(opts.strokeWidth){context.beginPath();context.moveTo(0,coords[0].y);for(i=0;i<coords.length;i++){context.lineTo(coords[i].x,coords[i].y);}
context.lineWidth=opts.strokeWidth*devicePixelRatio;context.strokeStyle=opts.strokeColour;context.stroke();}});peity.register('bar',{colours:["#4D89F9"],delimiter:",",height:16,max:null,min:0,spacing:devicePixelRatio,width:32},function(opts){var values=this.values()
var max=Math.max.apply(Math,values.concat([opts.max]));var min=Math.min.apply(Math,values.concat([opts.min]))
var canvas=this.prepareCanvas(opts.width,opts.height)
var context=this.context
var width=canvas.width
var height=canvas.height
var yQuotient=height/(max-min)
var space=opts.spacing
var xQuotient=(width+space)/values.length
var colours=this.colours()
for(var i=0;i<values.length;i++){var value=values[i]
var x=i*xQuotient
var y=height-(yQuotient*(value-min))
context.fillStyle=colours.call(this,value,i,values)
context.fillRect(x,y,xQuotient-space,yQuotient*values[i])}});})(jQuery,document,Math,window.devicePixelRatio||1);(function(B){B.color={};B.color.make=function(F,E,C,D){var G={};G.r=F||0;G.g=E||0;G.b=C||0;G.a=D!=null?D:1;G.add=function(J,I){for(var H=0;H<J.length;++H){G[J.charAt(H)]+=I}return G.normalize()};G.scale=function(J,I){for(var H=0;H<J.length;++H){G[J.charAt(H)]*=I}return G.normalize()};G.toString=function(){if(G.a>=1){return"rgb("+[G.r,G.g,G.b].join(",")+")"}else{return"rgba("+[G.r,G.g,G.b,G.a].join(",")+")"}};G.normalize=function(){function H(J,K,I){return K<J?J:(K>I?I:K)}G.r=H(0,parseInt(G.r),255);G.g=H(0,parseInt(G.g),255);G.b=H(0,parseInt(G.b),255);G.a=H(0,G.a,1);return G};G.clone=function(){return B.color.make(G.r,G.b,G.g,G.a)};return G.normalize()};B.color.extract=function(D,C){var E;do{E=D.css(C).toLowerCase();if(E!=""&&E!="transparent"){break}D=D.parent()}while(!B.nodeName(D.get(0),"body"));if(E=="rgba(0, 0, 0, 0)"){E="transparent"}return B.color.parse(E)};B.color.parse=function(F){var E,C=B.color.make;if(E=/rgb\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*\)/.exec(F)){return C(parseInt(E[1],10),parseInt(E[2],10),parseInt(E[3],10))}if(E=/rgba\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*,\s*([0-9]+(?:\.[0-9]+)?)\s*\)/.exec(F)){return C(parseInt(E[1],10),parseInt(E[2],10),parseInt(E[3],10),parseFloat(E[4]))}if(E=/rgb\(\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\%\s*\)/.exec(F)){return C(parseFloat(E[1])*2.55,parseFloat(E[2])*2.55,parseFloat(E[3])*2.55)}if(E=/rgba\(\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\s*\)/.exec(F)){return C(parseFloat(E[1])*2.55,parseFloat(E[2])*2.55,parseFloat(E[3])*2.55,parseFloat(E[4]))}if(E=/#([a-fA-F0-9]{2})([a-fA-F0-9]{2})([a-fA-F0-9]{2})/.exec(F)){return C(parseInt(E[1],16),parseInt(E[2],16),parseInt(E[3],16))}if(E=/#([a-fA-F0-9])([a-fA-F0-9])([a-fA-F0-9])/.exec(F)){return C(parseInt(E[1]+E[1],16),parseInt(E[2]+E[2],16),parseInt(E[3]+E[3],16))}var D=B.trim(F).toLowerCase();if(D=="transparent"){return C(255,255,255,0)}else{E=A[D]||[0,0,0];return C(E[0],E[1],E[2])}};var A={aqua:[0,255,255],azure:[240,255,255],beige:[245,245,220],black:[0,0,0],blue:[0,0,255],brown:[165,42,42],cyan:[0,255,255],darkblue:[0,0,139],darkcyan:[0,139,139],darkgrey:[169,169,169],darkgreen:[0,100,0],darkkhaki:[189,183,107],darkmagenta:[139,0,139],darkolivegreen:[85,107,47],darkorange:[255,140,0],darkorchid:[153,50,204],darkred:[139,0,0],darksalmon:[233,150,122],darkviolet:[148,0,211],fuchsia:[255,0,255],gold:[255,215,0],green:[0,128,0],indigo:[75,0,130],khaki:[240,230,140],lightblue:[173,216,230],lightcyan:[224,255,255],lightgreen:[144,238,144],lightgrey:[211,211,211],lightpink:[255,182,193],lightyellow:[255,255,224],lime:[0,255,0],magenta:[255,0,255],maroon:[128,0,0],navy:[0,0,128],olive:[128,128,0],orange:[255,165,0],pink:[255,192,203],purple:[128,0,128],violet:[128,0,128],red:[255,0,0],silver:[192,192,192],white:[255,255,255],yellow:[255,255,0]}})(jQuery);(function($){function Plot(placeholder,data_,options_,plugins){var series=[],options={colors:["#edc240","#afd8f8","#cb4b4b","#4da74d","#9440ed"],legend:{show:true,noColumns:1,labelFormatter:null,labelBoxBorderColor:"#ccc",container:null,position:"ne",margin:5,backgroundColor:null,backgroundOpacity:0.85,sorted:null},xaxis:{show:null,position:"bottom",mode:null,timezone:null,font:null,color:null,tickColor:null,transform:null,inverseTransform:null,min:null,max:null,autoscaleMargin:null,ticks:null,tickFormatter:null,labelWidth:null,labelHeight:null,reserveSpace:null,tickLength:null,alignTicksWithAxis:null,tickDecimals:null,tickSize:null,minTickSize:null,monthNames:null,timeformat:null,twelveHourClock:false},yaxis:{autoscaleMargin:0.02,position:"left"},xaxes:[],yaxes:[],series:{points:{show:false,radius:3,lineWidth:2,fill:true,fillColor:"#ffffff",symbol:"circle"},lines:{lineWidth:2,fill:false,fillColor:null,steps:false},bars:{show:false,lineWidth:2,barWidth:1,fill:true,fillColor:null,align:"left",horizontal:false},shadowSize:3,highlightColor:null},grid:{show:true,aboveData:false,color:"#545454",backgroundColor:null,borderColor:null,tickColor:null,margin:0,labelMargin:5,axisMargin:8,borderWidth:2,minBorderMargin:null,markings:null,markingsColor:"#f4f4f4",markingsLineWidth:2,clickable:false,hoverable:false,autoHighlight:true,mouseActiveRadius:10},interaction:{redrawOverlayInterval:1000/60},hooks:{}},canvas=null,overlay=null,eventHolder=null,ctx=null,octx=null,xaxes=[],yaxes=[],plotOffset={left:0,right:0,top:0,bottom:0},canvasWidth=0,canvasHeight=0,plotWidth=0,plotHeight=0,hooks={processOptions:[],processRawData:[],processDatapoints:[],processOffset:[],drawBackground:[],drawSeries:[],draw:[],bindEvents:[],drawOverlay:[],shutdown:[]},plot=this;plot.setData=setData;plot.setupGrid=setupGrid;plot.draw=draw;plot.getPlaceholder=function(){return placeholder;};plot.getCanvas=function(){return canvas;};plot.getPlotOffset=function(){return plotOffset;};plot.width=function(){return plotWidth;};plot.height=function(){return plotHeight;};plot.offset=function(){var o=eventHolder.offset();o.left+=plotOffset.left;o.top+=plotOffset.top;return o;};plot.getData=function(){return series;};plot.getAxes=function(){var res={},i;$.each(xaxes.concat(yaxes),function(_,axis){if(axis)
res[axis.direction+(axis.n!=1?axis.n:"")+"axis"]=axis;});return res;};plot.getXAxes=function(){return xaxes;};plot.getYAxes=function(){return yaxes;};plot.c2p=canvasToAxisCoords;plot.p2c=axisToCanvasCoords;plot.getOptions=function(){return options;};plot.highlight=highlight;plot.unhighlight=unhighlight;plot.triggerRedrawOverlay=triggerRedrawOverlay;plot.pointOffset=function(point){return{left:parseInt(xaxes[axisNumber(point,"x")-1].p2c(+point.x)+plotOffset.left,10),top:parseInt(yaxes[axisNumber(point,"y")-1].p2c(+point.y)+plotOffset.top,10)};};plot.shutdown=shutdown;plot.resize=function(){getCanvasDimensions();resizeCanvas(canvas);resizeCanvas(overlay);};plot.hooks=hooks;initPlugins(plot);parseOptions(options_);setupCanvases();setData(data_);setupGrid();draw();bindEvents();function executeHooks(hook,args){args=[plot].concat(args);for(var i=0;i<hook.length;++i)
hook[i].apply(this,args);}
function initPlugins(){for(var i=0;i<plugins.length;++i){var p=plugins[i];p.init(plot);if(p.options)
$.extend(true,options,p.options);}}
function parseOptions(opts){var i;$.extend(true,options,opts);if(options.xaxis.color==null)
options.xaxis.color=options.grid.color;if(options.yaxis.color==null)
options.yaxis.color=options.grid.color;if(options.xaxis.tickColor==null)
options.xaxis.tickColor=options.grid.tickColor;if(options.yaxis.tickColor==null)
options.yaxis.tickColor=options.grid.tickColor;if(options.grid.borderColor==null)
options.grid.borderColor=options.grid.color;if(options.grid.tickColor==null)
options.grid.tickColor=$.color.parse(options.grid.color).scale('a',0.22).toString();for(i=0;i<Math.max(1,options.xaxes.length);++i)
options.xaxes[i]=$.extend(true,{},options.xaxis,options.xaxes[i]);for(i=0;i<Math.max(1,options.yaxes.length);++i)
options.yaxes[i]=$.extend(true,{},options.yaxis,options.yaxes[i]);if(options.xaxis.noTicks&&options.xaxis.ticks==null)
options.xaxis.ticks=options.xaxis.noTicks;if(options.yaxis.noTicks&&options.yaxis.ticks==null)
options.yaxis.ticks=options.yaxis.noTicks;if(options.x2axis){options.xaxes[1]=$.extend(true,{},options.xaxis,options.x2axis);options.xaxes[1].position="top";}
if(options.y2axis){options.yaxes[1]=$.extend(true,{},options.yaxis,options.y2axis);options.yaxes[1].position="right";}
if(options.grid.coloredAreas)
options.grid.markings=options.grid.coloredAreas;if(options.grid.coloredAreasColor)
options.grid.markingsColor=options.grid.coloredAreasColor;if(options.lines)
$.extend(true,options.series.lines,options.lines);if(options.points)
$.extend(true,options.series.points,options.points);if(options.bars)
$.extend(true,options.series.bars,options.bars);if(options.shadowSize!=null)
options.series.shadowSize=options.shadowSize;if(options.highlightColor!=null)
options.series.highlightColor=options.highlightColor;for(i=0;i<options.xaxes.length;++i)
getOrCreateAxis(xaxes,i+1).options=options.xaxes[i];for(i=0;i<options.yaxes.length;++i)
getOrCreateAxis(yaxes,i+1).options=options.yaxes[i];for(var n in hooks)
if(options.hooks[n]&&options.hooks[n].length)
hooks[n]=hooks[n].concat(options.hooks[n]);executeHooks(hooks.processOptions,[options]);}
function setData(d){series=parseData(d);fillInSeriesOptions();processData();}
function parseData(d){var res=[];for(var i=0;i<d.length;++i){var s=$.extend(true,{},options.series);if(d[i].data!=null){s.data=d[i].data;delete d[i].data;$.extend(true,s,d[i]);d[i].data=s.data;}
else
s.data=d[i];res.push(s);}
return res;}
function axisNumber(obj,coord){var a=obj[coord+"axis"];if(typeof a=="object")
a=a.n;if(typeof a!="number")
a=1;return a;}
function allAxes(){return $.grep(xaxes.concat(yaxes),function(a){return a;});}
function canvasToAxisCoords(pos){var res={},i,axis;for(i=0;i<xaxes.length;++i){axis=xaxes[i];if(axis&&axis.used)
res["x"+axis.n]=axis.c2p(pos.left);}
for(i=0;i<yaxes.length;++i){axis=yaxes[i];if(axis&&axis.used)
res["y"+axis.n]=axis.c2p(pos.top);}
if(res.x1!==undefined)
res.x=res.x1;if(res.y1!==undefined)
res.y=res.y1;return res;}
function axisToCanvasCoords(pos){var res={},i,axis,key;for(i=0;i<xaxes.length;++i){axis=xaxes[i];if(axis&&axis.used){key="x"+axis.n;if(pos[key]==null&&axis.n==1)
key="x";if(pos[key]!=null){res.left=axis.p2c(pos[key]);break;}}}
for(i=0;i<yaxes.length;++i){axis=yaxes[i];if(axis&&axis.used){key="y"+axis.n;if(pos[key]==null&&axis.n==1)
key="y";if(pos[key]!=null){res.top=axis.p2c(pos[key]);break;}}}
return res;}
function getOrCreateAxis(axes,number){if(!axes[number-1])
axes[number-1]={n:number,direction:axes==xaxes?"x":"y",options:$.extend(true,{},axes==xaxes?options.xaxis:options.yaxis)};return axes[number-1];}
function fillInSeriesOptions(){var neededColors=series.length,maxIndex=0,i;for(i=0;i<series.length;++i){var sc=series[i].color;if(sc!=null){neededColors--;if(typeof sc=="number"&&sc>maxIndex){maxIndex=sc;}}}
if(maxIndex>neededColors){neededColors=maxIndex+1;}
var c,colors=[],colorPool=options.colors,colorPoolSize=colorPool.length,variation=0;for(i=0;i<neededColors;i++){c=$.color.parse(colorPool[i%colorPoolSize]||"#666");if(i%colorPoolSize==0&&i){if(variation>=0){if(variation<0.5){variation=-variation-0.2;}else variation=0;}else variation=-variation;}
colors[i]=c.scale('rgb',1+variation);}
var colori=0,s;for(i=0;i<series.length;++i){s=series[i];if(s.color==null){s.color=colors[colori].toString();++colori;}
else if(typeof s.color=="number")
s.color=colors[s.color].toString();if(s.lines.show==null){var v,show=true;for(v in s)
if(s[v]&&s[v].show){show=false;break;}
if(show)
s.lines.show=true;}
s.xaxis=getOrCreateAxis(xaxes,axisNumber(s,"x"));s.yaxis=getOrCreateAxis(yaxes,axisNumber(s,"y"));}}
function processData(){var topSentry=Number.POSITIVE_INFINITY,bottomSentry=Number.NEGATIVE_INFINITY,fakeInfinity=Number.MAX_VALUE,i,j,k,m,length,s,points,ps,x,y,axis,val,f,p,data,format;function updateAxis(axis,min,max){if(min<axis.datamin&&min!=-fakeInfinity)
axis.datamin=min;if(max>axis.datamax&&max!=fakeInfinity)
axis.datamax=max;}
$.each(allAxes(),function(_,axis){axis.datamin=topSentry;axis.datamax=bottomSentry;axis.used=false;});for(i=0;i<series.length;++i){s=series[i];s.datapoints={points:[]};executeHooks(hooks.processRawData,[s,s.data,s.datapoints]);}
for(i=0;i<series.length;++i){s=series[i];data=s.data;format=s.datapoints.format;if(!format){format=[];format.push({x:true,number:true,required:true});format.push({y:true,number:true,required:true});if(s.bars.show||(s.lines.show&&s.lines.fill)){format.push({y:true,number:true,required:false,defaultValue:0});if(s.bars.horizontal){delete format[format.length-1].y;format[format.length-1].x=true;}}
s.datapoints.format=format;}
if(s.datapoints.pointsize!=null)
continue;s.datapoints.pointsize=format.length;ps=s.datapoints.pointsize;points=s.datapoints.points;var insertSteps=s.lines.show&&s.lines.steps;s.xaxis.used=s.yaxis.used=true;for(j=k=0;j<data.length;++j,k+=ps){p=data[j];var nullify=p==null;if(!nullify){for(m=0;m<ps;++m){val=p[m];f=format[m];if(f){if(f.number&&val!=null){val=+val;if(isNaN(val))
val=null;else if(val==Infinity)
val=fakeInfinity;else if(val==-Infinity)
val=-fakeInfinity;}
if(val==null){if(f.required)
nullify=true;if(f.defaultValue!=null)
val=f.defaultValue;}}
points[k+m]=val;}}
if(nullify){for(m=0;m<ps;++m){val=points[k+m];if(val!=null){f=format[m];if(f.x)
updateAxis(s.xaxis,val,val);if(f.y)
updateAxis(s.yaxis,val,val);}
points[k+m]=null;}}
else{if(insertSteps&&k>0&&points[k-ps]!=null&&points[k-ps]!=points[k]&&points[k-ps+1]!=points[k+1]){for(m=0;m<ps;++m)
points[k+ps+m]=points[k+m];points[k+1]=points[k-ps+1];k+=ps;}}}}
for(i=0;i<series.length;++i){s=series[i];executeHooks(hooks.processDatapoints,[s,s.datapoints]);}
for(i=0;i<series.length;++i){s=series[i];points=s.datapoints.points,ps=s.datapoints.pointsize;format=s.datapoints.format;var xmin=topSentry,ymin=topSentry,xmax=bottomSentry,ymax=bottomSentry;for(j=0;j<points.length;j+=ps){if(points[j]==null)
continue;for(m=0;m<ps;++m){val=points[j+m];f=format[m];if(!f||val==fakeInfinity||val==-fakeInfinity)
continue;if(f.x){if(val<xmin)
xmin=val;if(val>xmax)
xmax=val;}
if(f.y){if(val<ymin)
ymin=val;if(val>ymax)
ymax=val;}}}
if(s.bars.show){var delta;switch(s.bars.align){case"left":delta=0;break;case"right":delta=-s.bars.barWidth;break;case"center":delta=-s.bars.barWidth/2;break;default:throw new Error("Invalid bar alignment: "+s.bars.align);}
if(s.bars.horizontal){ymin+=delta;ymax+=delta+s.bars.barWidth;}
else{xmin+=delta;xmax+=delta+s.bars.barWidth;}}
updateAxis(s.xaxis,xmin,xmax);updateAxis(s.yaxis,ymin,ymax);}
$.each(allAxes(),function(_,axis){if(axis.datamin==topSentry)
axis.datamin=null;if(axis.datamax==bottomSentry)
axis.datamax=null;});}
function getPixelRatio(cctx){var devicePixelRatio=window.devicePixelRatio||1;var backingStoreRatio=cctx.webkitBackingStorePixelRatio||cctx.mozBackingStorePixelRatio||cctx.msBackingStorePixelRatio||cctx.oBackingStorePixelRatio||cctx.backingStorePixelRatio||1;return devicePixelRatio/backingStoreRatio;}
function makeCanvas(skipPositioning,cls){var c=document.createElement('canvas');c.className=cls;if(!skipPositioning)
$(c).css({position:'absolute',left:0,top:0});$(c).appendTo(placeholder);if(!c.getContext){if(window.G_vmlCanvasManager){c=window.G_vmlCanvasManager.initElement(c);}else{throw new Error("Canvas is not available. If you're using IE with a fall-back such as Excanvas, then there's either a mistake in your conditional include, or the page has no DOCTYPE and is rendering in Quirks Mode.");}}
var cctx=c.getContext("2d");var pixelRatio=getPixelRatio(cctx);c.width=canvasWidth*pixelRatio;c.height=canvasHeight*pixelRatio;c.style.width=canvasWidth+"px";c.style.height=canvasHeight+"px";cctx.save();cctx.scale(pixelRatio,pixelRatio);return c;}
function getCanvasDimensions(){canvasWidth=placeholder.width();canvasHeight=placeholder.height();if(canvasWidth<=0||canvasHeight<=0)
throw new Error("Invalid dimensions for plot, width = "+canvasWidth+", height = "+canvasHeight);}
function resizeCanvas(c){var cctx=c.getContext("2d");var pixelRatio=getPixelRatio(cctx);if(c.style.width!=canvasWidth){c.width=canvasWidth*pixelRatio;c.style.width=canvasWidth+"px";}
if(c.style.height!=canvasHeight){c.height=canvasHeight*pixelRatio;c.style.height=canvasHeight+"px";}
cctx.restore();cctx.save();cctx.scale(pixelRatio,pixelRatio);}
function setupCanvases(){var reused,existingCanvas=placeholder.children("canvas.flot-base"),existingOverlay=placeholder.children("canvas.flot-overlay");if(existingCanvas.length==0||existingOverlay==0){placeholder.html("");placeholder.css({padding:0});if(placeholder.css("position")=='static')
placeholder.css("position","relative");getCanvasDimensions();canvas=makeCanvas(true,"flot-base");overlay=makeCanvas(false,"flot-overlay");reused=false;}
else{canvas=existingCanvas.get(0);overlay=existingOverlay.get(0);reused=true;}
ctx=canvas.getContext("2d");octx=overlay.getContext("2d");eventHolder=$(overlay);if(reused){placeholder.data("plot").shutdown();plot.resize();octx.clearRect(0,0,canvasWidth,canvasHeight);eventHolder.unbind();placeholder.children().not([canvas,overlay]).remove();}
placeholder.data("plot",plot);}
function bindEvents(){if(options.grid.hoverable){eventHolder.mousemove(onMouseMove);eventHolder.mouseleave(onMouseLeave);}
if(options.grid.clickable)
eventHolder.click(onClick);executeHooks(hooks.bindEvents,[eventHolder]);}
function shutdown(){if(redrawTimeout)
clearTimeout(redrawTimeout);eventHolder.unbind("mousemove",onMouseMove);eventHolder.unbind("mouseleave",onMouseLeave);eventHolder.unbind("click",onClick);executeHooks(hooks.shutdown,[eventHolder]);}
function setTransformationHelpers(axis){function identity(x){return x;}
var s,m,t=axis.options.transform||identity,it=axis.options.inverseTransform;if(axis.direction=="x"){s=axis.scale=plotWidth/Math.abs(t(axis.max)-t(axis.min));m=Math.min(t(axis.max),t(axis.min));}
else{s=axis.scale=plotHeight/Math.abs(t(axis.max)-t(axis.min));s=-s;m=Math.max(t(axis.max),t(axis.min));}
if(t==identity)
axis.p2c=function(p){return(p-m)*s;};else
axis.p2c=function(p){return(t(p)-m)*s;};if(!it)
axis.c2p=function(c){return m+c/s;};else
axis.c2p=function(c){return it(m+c/s);};}
function measureTickLabels(axis){var opts=axis.options,ticks=axis.ticks||[],axisw=opts.labelWidth||0,axish=opts.labelHeight||0,f=axis.font;ctx.save();ctx.font=f.style+" "+f.variant+" "+f.weight+" "+f.size+"px '"+f.family+"'";for(var i=0;i<ticks.length;++i){var t=ticks[i];t.lines=[];t.width=t.height=0;if(!t.label)
continue;var lines=(t.label+"").replace(/<br ?\/?>|\r\n|\r/g,"\n").split("\n");for(var j=0;j<lines.length;++j){var line={text:lines[j]},m=ctx.measureText(line.text);line.width=m.width;line.height=m.height!=null?m.height:f.size;line.height+=Math.round(f.size*0.15);t.width=Math.max(line.width,t.width);t.height+=line.height;t.lines.push(line);}
if(opts.labelWidth==null)
axisw=Math.max(axisw,t.width);if(opts.labelHeight==null)
axish=Math.max(axish,t.height);}
ctx.restore();axis.labelWidth=Math.ceil(axisw);axis.labelHeight=Math.ceil(axish);}
function allocateAxisBoxFirstPhase(axis){var lw=axis.labelWidth,lh=axis.labelHeight,pos=axis.options.position,tickLength=axis.options.tickLength,axisMargin=options.grid.axisMargin,padding=options.grid.labelMargin,all=axis.direction=="x"?xaxes:yaxes,index,innermost;var samePosition=$.grep(all,function(a){return a&&a.options.position==pos&&a.reserveSpace;});if($.inArray(axis,samePosition)==samePosition.length-1)
axisMargin=0;if(tickLength==null){var sameDirection=$.grep(all,function(a){return a&&a.reserveSpace;});innermost=$.inArray(axis,sameDirection)==0;if(innermost)
tickLength="full";else
tickLength=5;}
if(!isNaN(+tickLength))
padding+=+tickLength;if(axis.direction=="x"){lh+=padding;if(pos=="bottom"){plotOffset.bottom+=lh+axisMargin;axis.box={top:canvasHeight-plotOffset.bottom,height:lh};}
else{axis.box={top:plotOffset.top+axisMargin,height:lh};plotOffset.top+=lh+axisMargin;}}
else{lw+=padding;if(pos=="left"){axis.box={left:plotOffset.left+axisMargin,width:lw};plotOffset.left+=lw+axisMargin;}
else{plotOffset.right+=lw+axisMargin;axis.box={left:canvasWidth-plotOffset.right,width:lw};}}
axis.position=pos;axis.tickLength=tickLength;axis.box.padding=padding;axis.innermost=innermost;}
function allocateAxisBoxSecondPhase(axis){if(axis.direction=="x"){axis.box.left=plotOffset.left-axis.labelWidth/2;axis.box.width=canvasWidth-plotOffset.left-plotOffset.right+axis.labelWidth;}
else{axis.box.top=plotOffset.top-axis.labelHeight/2;axis.box.height=canvasHeight-plotOffset.bottom-plotOffset.top+axis.labelHeight;}}
function adjustLayoutForThingsStickingOut(){var minMargin=options.grid.minBorderMargin,margins={x:0,y:0},i,axis;if(minMargin==null){minMargin=0;for(i=0;i<series.length;++i)
minMargin=Math.max(minMargin,2*(series[i].points.radius+series[i].points.lineWidth/2));}
margins.x=margins.y=Math.ceil(minMargin);$.each(allAxes(),function(_,axis){var dir=axis.direction;if(axis.reserveSpace)
margins[dir]=Math.ceil(Math.max(margins[dir],(dir=="x"?axis.labelWidth:axis.labelHeight)/2));});plotOffset.left=Math.max(margins.x,plotOffset.left);plotOffset.right=Math.max(margins.x,plotOffset.right);plotOffset.top=Math.max(margins.y,plotOffset.top);plotOffset.bottom=Math.max(margins.y,plotOffset.bottom);}
function setupGrid(){var i,axes=allAxes(),showGrid=options.grid.show;for(var a in plotOffset){var margin=options.grid.margin||0;plotOffset[a]=typeof margin=="number"?margin:margin[a]||0;}
executeHooks(hooks.processOffset,[plotOffset]);for(var a in plotOffset){if(typeof(options.grid.borderWidth)=="object"){plotOffset[a]=showGrid?options.grid.borderWidth[a]:0;}
else{plotOffset[a]=showGrid?options.grid.borderWidth:0;}}
$.each(axes,function(_,axis){axis.show=axis.options.show;if(axis.show==null)
axis.show=axis.used;axis.reserveSpace=axis.show||axis.options.reserveSpace;setRange(axis);});if(showGrid){var fontDefaults={style:placeholder.css("font-style"),size:Math.round(0.8*(+placeholder.css("font-size").replace("px","")||13)),variant:placeholder.css("font-variant"),weight:placeholder.css("font-weight"),family:placeholder.css("font-family")};var allocatedAxes=$.grep(axes,function(axis){return axis.reserveSpace;});$.each(allocatedAxes,function(_,axis){setupTickGeneration(axis);setTicks(axis);snapRangeToTicks(axis,axis.ticks);axis.font=$.extend({},fontDefaults,axis.options.font);measureTickLabels(axis);});for(i=allocatedAxes.length-1;i>=0;--i)
allocateAxisBoxFirstPhase(allocatedAxes[i]);adjustLayoutForThingsStickingOut();$.each(allocatedAxes,function(_,axis){allocateAxisBoxSecondPhase(axis);});}
plotWidth=canvasWidth-plotOffset.left-plotOffset.right;plotHeight=canvasHeight-plotOffset.bottom-plotOffset.top;$.each(axes,function(_,axis){setTransformationHelpers(axis);});insertLegend();}
function setRange(axis){var opts=axis.options,min=+(opts.min!=null?opts.min:axis.datamin),max=+(opts.max!=null?opts.max:axis.datamax),delta=max-min;if(delta==0.0){var widen=max==0?1:0.01;if(opts.min==null)
min-=widen;if(opts.max==null||opts.min!=null)
max+=widen;}
else{var margin=opts.autoscaleMargin;if(margin!=null){if(opts.min==null){min-=delta*margin;if(min<0&&axis.datamin!=null&&axis.datamin>=0)
min=0;}
if(opts.max==null){max+=delta*margin;if(max>0&&axis.datamax!=null&&axis.datamax<=0)
max=0;}}}
axis.min=min;axis.max=max;}
function setupTickGeneration(axis){var opts=axis.options;var noTicks;if(typeof opts.ticks=="number"&&opts.ticks>0)
noTicks=opts.ticks;else
noTicks=0.3*Math.sqrt(axis.direction=="x"?canvasWidth:canvasHeight);axis.delta=(axis.max-axis.min)/noTicks;if(opts.mode=="time"&&!axis.tickGenerator){throw new Error("Time mode requires the flot.time plugin.");}
if(!axis.tickGenerator){var maxDec=opts.tickDecimals;var dec=-Math.floor(Math.log(axis.delta)/Math.LN10);if(maxDec!=null&&dec>maxDec)
dec=maxDec;var magn=Math.pow(10,-dec);var norm=axis.delta/magn;var size;if(norm<1.5)
size=1;else if(norm<3){size=2;if(norm>2.25&&(maxDec==null||dec+1<=maxDec)){size=2.5;++dec;}}
else if(norm<7.5)
size=5;else size=10;size*=magn;if(opts.minTickSize!=null&&size<opts.minTickSize)
size=opts.minTickSize;axis.tickDecimals=Math.max(0,maxDec!=null?maxDec:dec);axis.tickSize=opts.tickSize||size;axis.tickGenerator=function(axis){var ticks=[],start=floorInBase(axis.min,axis.tickSize),i=0,v=Number.NaN,prev;do{prev=v;v=start+i*axis.tickSize;ticks.push(v);++i;}while(v<axis.max&&v!=prev);return ticks;};axis.tickFormatter=function(value,axis){var factor=Math.pow(10,axis.tickDecimals);var formatted=""+Math.round(value*factor)/factor;if(axis.tickDecimals!=null){var decimal=formatted.indexOf(".");var precision=decimal==-1?0:formatted.length-decimal-1;if(precision<axis.tickDecimals){return(precision?formatted:formatted+".")+(""+factor).substr(1,axis.tickDecimals-precision);}}
return formatted;};}
if($.isFunction(opts.tickFormatter))
axis.tickFormatter=function(v,axis){return""+opts.tickFormatter(v,axis);};if(opts.alignTicksWithAxis!=null){var otherAxis=(axis.direction=="x"?xaxes:yaxes)[opts.alignTicksWithAxis-1];if(otherAxis&&otherAxis.used&&otherAxis!=axis){var niceTicks=axis.tickGenerator(axis);if(niceTicks.length>0){if(opts.min==null)
axis.min=Math.min(axis.min,niceTicks[0]);if(opts.max==null&&niceTicks.length>1)
axis.max=Math.max(axis.max,niceTicks[niceTicks.length-1]);}
axis.tickGenerator=function(axis){var ticks=[],v,i;for(i=0;i<otherAxis.ticks.length;++i){v=(otherAxis.ticks[i].v-otherAxis.min)/(otherAxis.max-otherAxis.min);v=axis.min+v*(axis.max-axis.min);ticks.push(v);}
return ticks;};if(!axis.mode&&opts.tickDecimals==null){var extraDec=Math.max(0,-Math.floor(Math.log(axis.delta)/Math.LN10)+1),ts=axis.tickGenerator(axis);if(!(ts.length>1&&/\..*0$/.test((ts[1]-ts[0]).toFixed(extraDec))))
axis.tickDecimals=extraDec;}}}}
function setTicks(axis){var oticks=axis.options.ticks,ticks=[];if(oticks==null||(typeof oticks=="number"&&oticks>0))
ticks=axis.tickGenerator(axis);else if(oticks){if($.isFunction(oticks))
ticks=oticks(axis);else
ticks=oticks;}
var i,v;axis.ticks=[];for(i=0;i<ticks.length;++i){var label=null;var t=ticks[i];if(typeof t=="object"){v=+t[0];if(t.length>1)
label=t[1];}
else
v=+t;if(label==null)
label=axis.tickFormatter(v,axis);if(!isNaN(v))
axis.ticks.push({v:v,label:label});}}
function snapRangeToTicks(axis,ticks){if(axis.options.autoscaleMargin&&ticks.length>0){if(axis.options.min==null)
axis.min=Math.min(axis.min,ticks[0].v);if(axis.options.max==null&&ticks.length>1)
axis.max=Math.max(axis.max,ticks[ticks.length-1].v);}}
function draw(){ctx.clearRect(0,0,canvasWidth,canvasHeight);executeHooks(hooks.drawBackground,[ctx]);var grid=options.grid;if(grid.show&&grid.backgroundColor)
drawBackground();if(grid.show&&!grid.aboveData){drawGrid();drawAxisLabels();}
for(var i=0;i<series.length;++i){executeHooks(hooks.drawSeries,[ctx,series[i]]);drawSeries(series[i]);}
executeHooks(hooks.draw,[ctx]);if(grid.show&&grid.aboveData){drawGrid();drawAxisLabels();}}
function extractRange(ranges,coord){var axis,from,to,key,axes=allAxes();for(var i=0;i<axes.length;++i){axis=axes[i];if(axis.direction==coord){key=coord+axis.n+"axis";if(!ranges[key]&&axis.n==1)
key=coord+"axis";if(ranges[key]){from=ranges[key].from;to=ranges[key].to;break;}}}
if(!ranges[key]){axis=coord=="x"?xaxes[0]:yaxes[0];from=ranges[coord+"1"];to=ranges[coord+"2"];}
if(from!=null&&to!=null&&from>to){var tmp=from;from=to;to=tmp;}
return{from:from,to:to,axis:axis};}
function drawBackground(){ctx.save();ctx.translate(plotOffset.left,plotOffset.top);ctx.fillStyle=getColorOrGradient(options.grid.backgroundColor,plotHeight,0,"rgba(255, 255, 255, 0)");ctx.fillRect(0,0,plotWidth,plotHeight);ctx.restore();}
function drawGrid(){var i,axes,bw,bc;ctx.save();ctx.translate(plotOffset.left,plotOffset.top);var markings=options.grid.markings;if(markings){if($.isFunction(markings)){axes=plot.getAxes();axes.xmin=axes.xaxis.min;axes.xmax=axes.xaxis.max;axes.ymin=axes.yaxis.min;axes.ymax=axes.yaxis.max;markings=markings(axes);}
for(i=0;i<markings.length;++i){var m=markings[i],xrange=extractRange(m,"x"),yrange=extractRange(m,"y");if(xrange.from==null)
xrange.from=xrange.axis.min;if(xrange.to==null)
xrange.to=xrange.axis.max;if(yrange.from==null)
yrange.from=yrange.axis.min;if(yrange.to==null)
yrange.to=yrange.axis.max;if(xrange.to<xrange.axis.min||xrange.from>xrange.axis.max||yrange.to<yrange.axis.min||yrange.from>yrange.axis.max)
continue;xrange.from=Math.max(xrange.from,xrange.axis.min);xrange.to=Math.min(xrange.to,xrange.axis.max);yrange.from=Math.max(yrange.from,yrange.axis.min);yrange.to=Math.min(yrange.to,yrange.axis.max);if(xrange.from==xrange.to&&yrange.from==yrange.to)
continue;xrange.from=xrange.axis.p2c(xrange.from);xrange.to=xrange.axis.p2c(xrange.to);yrange.from=yrange.axis.p2c(yrange.from);yrange.to=yrange.axis.p2c(yrange.to);if(xrange.from==xrange.to||yrange.from==yrange.to){ctx.beginPath();ctx.strokeStyle=m.color||options.grid.markingsColor;ctx.lineWidth=m.lineWidth||options.grid.markingsLineWidth;ctx.moveTo(xrange.from,yrange.from);ctx.lineTo(xrange.to,yrange.to);ctx.stroke();}
else{ctx.fillStyle=m.color||options.grid.markingsColor;ctx.fillRect(xrange.from,yrange.to,xrange.to-xrange.from,yrange.from-yrange.to);}}}
axes=allAxes();bw=options.grid.borderWidth;for(var j=0;j<axes.length;++j){var axis=axes[j],box=axis.box,t=axis.tickLength,x,y,xoff,yoff;if(!axis.show||axis.ticks.length==0)
continue;ctx.strokeStyle=axis.options.tickColor||$.color.parse(axis.options.color).scale('a',0.22).toString();ctx.lineWidth=1;if(axis.direction=="x"){x=0;if(t=="full")
y=(axis.position=="top"?0:plotHeight);else
y=box.top-plotOffset.top+(axis.position=="top"?box.height:0);}
else{y=0;if(t=="full")
x=(axis.position=="left"?0:plotWidth);else
x=box.left-plotOffset.left+(axis.position=="left"?box.width:0);}
if(!axis.innermost){ctx.beginPath();xoff=yoff=0;if(axis.direction=="x")
xoff=plotWidth;else
yoff=plotHeight;if(ctx.lineWidth==1){x=Math.floor(x)+0.5;y=Math.floor(y)+0.5;}
ctx.moveTo(x,y);ctx.lineTo(x+xoff,y+yoff);ctx.stroke();}
ctx.beginPath();for(i=0;i<axis.ticks.length;++i){var v=axis.ticks[i].v;xoff=yoff=0;if(v<axis.min||v>axis.max||(t=="full"&&((typeof bw=="object"&&bw[axis.position]>0)||bw>0)&&(v==axis.min||v==axis.max)))
continue;if(axis.direction=="x"){x=axis.p2c(v);yoff=t=="full"?-plotHeight:t;if(axis.position=="top")
yoff=-yoff;}
else{y=axis.p2c(v);xoff=t=="full"?-plotWidth:t;if(axis.position=="left")
xoff=-xoff;}
if(ctx.lineWidth==1){if(axis.direction=="x")
x=Math.floor(x)+0.5;else
y=Math.floor(y)+0.5;}
ctx.moveTo(x,y);ctx.lineTo(x+xoff,y+yoff);}
ctx.stroke();}
if(bw){bc=options.grid.borderColor;if(typeof bw=="object"||typeof bc=="object"){if(typeof bw!=="object"){bw={top:bw,right:bw,bottom:bw,left:bw};}
if(typeof bc!=="object"){bc={top:bc,right:bc,bottom:bc,left:bc};}
if(bw.top>0){ctx.strokeStyle=bc.top;ctx.lineWidth=bw.top;ctx.beginPath();ctx.moveTo(0-bw.left,0-bw.top/2);ctx.lineTo(plotWidth,0-bw.top/2);ctx.stroke();}
if(bw.right>0){ctx.strokeStyle=bc.right;ctx.lineWidth=bw.right;ctx.beginPath();ctx.moveTo(plotWidth+bw.right/2,0-bw.top);ctx.lineTo(plotWidth+bw.right/2,plotHeight);ctx.stroke();}
if(bw.bottom>0){ctx.strokeStyle=bc.bottom;ctx.lineWidth=bw.bottom;ctx.beginPath();ctx.moveTo(plotWidth+bw.right,plotHeight+bw.bottom/2);ctx.lineTo(0,plotHeight+bw.bottom/2);ctx.stroke();}
if(bw.left>0){ctx.strokeStyle=bc.left;ctx.lineWidth=bw.left;ctx.beginPath();ctx.moveTo(0-bw.left/2,plotHeight+bw.bottom);ctx.lineTo(0-bw.left/2,0);ctx.stroke();}}
else{ctx.lineWidth=bw;ctx.strokeStyle=options.grid.borderColor;ctx.strokeRect(-bw/2,-bw/2,plotWidth+bw,plotHeight+bw);}}
ctx.restore();}
function drawAxisLabels(){ctx.save();$.each(allAxes(),function(_,axis){if(!axis.show||axis.ticks.length==0)
return;var box=axis.box,f=axis.font;ctx.fillStyle=axis.options.color;ctx.font=f.style+" "+f.variant+" "+f.weight+" "+f.size+"px "+f.family;ctx.textAlign="start";ctx.textBaseline="middle";for(var i=0;i<axis.ticks.length;++i){var tick=axis.ticks[i];if(!tick.label||tick.v<axis.min||tick.v>axis.max)
continue;var x,y,offset=0,line;for(var k=0;k<tick.lines.length;++k){line=tick.lines[k];if(axis.direction=="x"){x=plotOffset.left+axis.p2c(tick.v)-line.width/2;if(axis.position=="bottom")
y=box.top+box.padding;else
y=box.top+box.height-box.padding-tick.height;}
else{y=plotOffset.top+axis.p2c(tick.v)-tick.height/2;if(axis.position=="left")
x=box.left+box.width-box.padding-line.width;else
x=box.left+box.padding;}
y+=line.height/2+offset;offset+=line.height;if($.browser.opera){x=Math.floor(x);y=Math.ceil(y-2);}
ctx.fillText(line.text,x,y);}}});ctx.restore();}
function drawSeries(series){if(series.lines.show)
drawSeriesLines(series);if(series.bars.show)
drawSeriesBars(series);if(series.points.show)
drawSeriesPoints(series);}
function drawSeriesLines(series){function plotLine(datapoints,xoffset,yoffset,axisx,axisy){var points=datapoints.points,ps=datapoints.pointsize,prevx=null,prevy=null;ctx.beginPath();for(var i=ps;i<points.length;i+=ps){var x1=points[i-ps],y1=points[i-ps+1],x2=points[i],y2=points[i+1];if(x1==null||x2==null)
continue;if(y1<=y2&&y1<axisy.min){if(y2<axisy.min)
continue;x1=(axisy.min-y1)/(y2-y1)*(x2-x1)+x1;y1=axisy.min;}
else if(y2<=y1&&y2<axisy.min){if(y1<axisy.min)
continue;x2=(axisy.min-y1)/(y2-y1)*(x2-x1)+x1;y2=axisy.min;}
if(y1>=y2&&y1>axisy.max){if(y2>axisy.max)
continue;x1=(axisy.max-y1)/(y2-y1)*(x2-x1)+x1;y1=axisy.max;}
else if(y2>=y1&&y2>axisy.max){if(y1>axisy.max)
continue;x2=(axisy.max-y1)/(y2-y1)*(x2-x1)+x1;y2=axisy.max;}
if(x1<=x2&&x1<axisx.min){if(x2<axisx.min)
continue;y1=(axisx.min-x1)/(x2-x1)*(y2-y1)+y1;x1=axisx.min;}
else if(x2<=x1&&x2<axisx.min){if(x1<axisx.min)
continue;y2=(axisx.min-x1)/(x2-x1)*(y2-y1)+y1;x2=axisx.min;}
if(x1>=x2&&x1>axisx.max){if(x2>axisx.max)
continue;y1=(axisx.max-x1)/(x2-x1)*(y2-y1)+y1;x1=axisx.max;}
else if(x2>=x1&&x2>axisx.max){if(x1>axisx.max)
continue;y2=(axisx.max-x1)/(x2-x1)*(y2-y1)+y1;x2=axisx.max;}
if(x1!=prevx||y1!=prevy)
ctx.moveTo(axisx.p2c(x1)+xoffset,axisy.p2c(y1)+yoffset);prevx=x2;prevy=y2;ctx.lineTo(axisx.p2c(x2)+xoffset,axisy.p2c(y2)+yoffset);}
ctx.stroke();}
function plotLineArea(datapoints,axisx,axisy){var points=datapoints.points,ps=datapoints.pointsize,bottom=Math.min(Math.max(0,axisy.min),axisy.max),i=0,top,areaOpen=false,ypos=1,segmentStart=0,segmentEnd=0;while(true){if(ps>0&&i>points.length+ps)
break;i+=ps;var x1=points[i-ps],y1=points[i-ps+ypos],x2=points[i],y2=points[i+ypos];if(areaOpen){if(ps>0&&x1!=null&&x2==null){segmentEnd=i;ps=-ps;ypos=2;continue;}
if(ps<0&&i==segmentStart+ps){ctx.fill();areaOpen=false;ps=-ps;ypos=1;i=segmentStart=segmentEnd+ps;continue;}}
if(x1==null||x2==null)
continue;if(x1<=x2&&x1<axisx.min){if(x2<axisx.min)
continue;y1=(axisx.min-x1)/(x2-x1)*(y2-y1)+y1;x1=axisx.min;}
else if(x2<=x1&&x2<axisx.min){if(x1<axisx.min)
continue;y2=(axisx.min-x1)/(x2-x1)*(y2-y1)+y1;x2=axisx.min;}
if(x1>=x2&&x1>axisx.max){if(x2>axisx.max)
continue;y1=(axisx.max-x1)/(x2-x1)*(y2-y1)+y1;x1=axisx.max;}
else if(x2>=x1&&x2>axisx.max){if(x1>axisx.max)
continue;y2=(axisx.max-x1)/(x2-x1)*(y2-y1)+y1;x2=axisx.max;}
if(!areaOpen){ctx.beginPath();ctx.moveTo(axisx.p2c(x1),axisy.p2c(bottom));areaOpen=true;}
if(y1>=axisy.max&&y2>=axisy.max){ctx.lineTo(axisx.p2c(x1),axisy.p2c(axisy.max));ctx.lineTo(axisx.p2c(x2),axisy.p2c(axisy.max));continue;}
else if(y1<=axisy.min&&y2<=axisy.min){ctx.lineTo(axisx.p2c(x1),axisy.p2c(axisy.min));ctx.lineTo(axisx.p2c(x2),axisy.p2c(axisy.min));continue;}
var x1old=x1,x2old=x2;if(y1<=y2&&y1<axisy.min&&y2>=axisy.min){x1=(axisy.min-y1)/(y2-y1)*(x2-x1)+x1;y1=axisy.min;}
else if(y2<=y1&&y2<axisy.min&&y1>=axisy.min){x2=(axisy.min-y1)/(y2-y1)*(x2-x1)+x1;y2=axisy.min;}
if(y1>=y2&&y1>axisy.max&&y2<=axisy.max){x1=(axisy.max-y1)/(y2-y1)*(x2-x1)+x1;y1=axisy.max;}
else if(y2>=y1&&y2>axisy.max&&y1<=axisy.max){x2=(axisy.max-y1)/(y2-y1)*(x2-x1)+x1;y2=axisy.max;}
if(x1!=x1old){ctx.lineTo(axisx.p2c(x1old),axisy.p2c(y1));}
ctx.lineTo(axisx.p2c(x1),axisy.p2c(y1));ctx.lineTo(axisx.p2c(x2),axisy.p2c(y2));if(x2!=x2old){ctx.lineTo(axisx.p2c(x2),axisy.p2c(y2));ctx.lineTo(axisx.p2c(x2old),axisy.p2c(y2));}}}
ctx.save();ctx.translate(plotOffset.left,plotOffset.top);ctx.lineJoin="round";var lw=series.lines.lineWidth,sw=series.shadowSize;if(lw>0&&sw>0){ctx.lineWidth=sw;ctx.strokeStyle="rgba(0,0,0,0.1)";var angle=Math.PI/18;plotLine(series.datapoints,Math.sin(angle)*(lw/2+sw/2),Math.cos(angle)*(lw/2+sw/2),series.xaxis,series.yaxis);ctx.lineWidth=sw/2;plotLine(series.datapoints,Math.sin(angle)*(lw/2+sw/4),Math.cos(angle)*(lw/2+sw/4),series.xaxis,series.yaxis);}
ctx.lineWidth=lw;ctx.strokeStyle=series.color;var fillStyle=getFillStyle(series.lines,series.color,0,plotHeight);if(fillStyle){ctx.fillStyle=fillStyle;plotLineArea(series.datapoints,series.xaxis,series.yaxis);}
if(lw>0)
plotLine(series.datapoints,0,0,series.xaxis,series.yaxis);ctx.restore();}
function drawSeriesPoints(series){function plotPoints(datapoints,radius,fillStyle,offset,shadow,axisx,axisy,symbol){var points=datapoints.points,ps=datapoints.pointsize;for(var i=0;i<points.length;i+=ps){var x=points[i],y=points[i+1];if(x==null||x<axisx.min||x>axisx.max||y<axisy.min||y>axisy.max)
continue;ctx.beginPath();x=axisx.p2c(x);y=axisy.p2c(y)+offset;if(symbol=="circle")
ctx.arc(x,y,radius,0,shadow?Math.PI:Math.PI*2,false);else
symbol(ctx,x,y,radius,shadow);ctx.closePath();if(fillStyle){ctx.fillStyle=fillStyle;ctx.fill();}
ctx.stroke();}}
ctx.save();ctx.translate(plotOffset.left,plotOffset.top);var lw=series.points.lineWidth,sw=series.shadowSize,radius=series.points.radius,symbol=series.points.symbol;if(lw>0&&sw>0){var w=sw/2;ctx.lineWidth=w;ctx.strokeStyle="rgba(0,0,0,0.1)";plotPoints(series.datapoints,radius,null,w+w/2,true,series.xaxis,series.yaxis,symbol);ctx.strokeStyle="rgba(0,0,0,0.2)";plotPoints(series.datapoints,radius,null,w/2,true,series.xaxis,series.yaxis,symbol);}
ctx.lineWidth=lw;ctx.strokeStyle=series.color;plotPoints(series.datapoints,radius,getFillStyle(series.points,series.color),0,false,series.xaxis,series.yaxis,symbol);ctx.restore();}
function drawBar(x,y,b,barLeft,barRight,offset,fillStyleCallback,axisx,axisy,c,horizontal,lineWidth){var left,right,bottom,top,drawLeft,drawRight,drawTop,drawBottom,tmp;if(horizontal){drawBottom=drawRight=drawTop=true;drawLeft=false;left=b;right=x;top=y+barLeft;bottom=y+barRight;if(right<left){tmp=right;right=left;left=tmp;drawLeft=true;drawRight=false;}}
else{drawLeft=drawRight=drawTop=true;drawBottom=false;left=x+barLeft;right=x+barRight;bottom=b;top=y;if(top<bottom){tmp=top;top=bottom;bottom=tmp;drawBottom=true;drawTop=false;}}
if(right<axisx.min||left>axisx.max||top<axisy.min||bottom>axisy.max)
return;if(left<axisx.min){left=axisx.min;drawLeft=false;}
if(right>axisx.max){right=axisx.max;drawRight=false;}
if(bottom<axisy.min){bottom=axisy.min;drawBottom=false;}
if(top>axisy.max){top=axisy.max;drawTop=false;}
left=axisx.p2c(left);bottom=axisy.p2c(bottom);right=axisx.p2c(right);top=axisy.p2c(top);if(fillStyleCallback){c.beginPath();c.moveTo(left,bottom);c.lineTo(left,top);c.lineTo(right,top);c.lineTo(right,bottom);c.fillStyle=fillStyleCallback(bottom,top);c.fill();}
if(lineWidth>0&&(drawLeft||drawRight||drawTop||drawBottom)){c.beginPath();c.moveTo(left,bottom+offset);if(drawLeft)
c.lineTo(left,top+offset);else
c.moveTo(left,top+offset);if(drawTop)
c.lineTo(right,top+offset);else
c.moveTo(right,top+offset);if(drawRight)
c.lineTo(right,bottom+offset);else
c.moveTo(right,bottom+offset);if(drawBottom)
c.lineTo(left,bottom+offset);else
c.moveTo(left,bottom+offset);c.stroke();}}
function drawSeriesBars(series){function plotBars(datapoints,barLeft,barRight,offset,fillStyleCallback,axisx,axisy){var points=datapoints.points,ps=datapoints.pointsize;for(var i=0;i<points.length;i+=ps){if(points[i]==null)
continue;drawBar(points[i],points[i+1],points[i+2],barLeft,barRight,offset,fillStyleCallback,axisx,axisy,ctx,series.bars.horizontal,series.bars.lineWidth);}}
ctx.save();ctx.translate(plotOffset.left,plotOffset.top);ctx.lineWidth=series.bars.lineWidth;ctx.strokeStyle=series.color;var barLeft;switch(series.bars.align){case"left":barLeft=0;break;case"right":barLeft=-series.bars.barWidth;break;case"center":barLeft=-series.bars.barWidth/2;break;default:throw new Error("Invalid bar alignment: "+series.bars.align);}
var fillStyleCallback=series.bars.fill?function(bottom,top){return getFillStyle(series.bars,series.color,bottom,top);}:null;plotBars(series.datapoints,barLeft,barLeft+series.bars.barWidth,0,fillStyleCallback,series.xaxis,series.yaxis);ctx.restore();}
function getFillStyle(filloptions,seriesColor,bottom,top){var fill=filloptions.fill;if(!fill)
return null;if(filloptions.fillColor)
return getColorOrGradient(filloptions.fillColor,bottom,top,seriesColor);var c=$.color.parse(seriesColor);c.a=typeof fill=="number"?fill:0.4;c.normalize();return c.toString();}
function insertLegend(){placeholder.find(".legend").remove();if(!options.legend.show)
return;var fragments=[],entries=[],rowStarted=false,lf=options.legend.labelFormatter,s,label;for(var i=0;i<series.length;++i){s=series[i];if(s.label){label=lf?lf(s.label,s):s.label;if(label){entries.push({label:label,color:s.color});}}}
if(options.legend.sorted){if($.isFunction(options.legend.sorted)){entries.sort(options.legend.sorted);}else{var ascending=options.legend.sorted!="descending";entries.sort(function(a,b){return a.label==b.label?0:((a.label<b.label)!=ascending?1:-1);});}}
for(var i=0;i<entries.length;++i){var entry=entries[i];if(i%options.legend.noColumns==0){if(rowStarted)
fragments.push('</tr>');fragments.push('<tr>');rowStarted=true;}
fragments.push('<td class="legendColorBox"><div style="border:1px solid '+options.legend.labelBoxBorderColor+';padding:1px"><div style="width:4px;height:0;border:5px solid '+entry.color+';overflow:hidden"></div></div></td>'+'<td class="legendLabel">'+entry.label+'</td>');}
if(rowStarted)
fragments.push('</tr>');if(fragments.length==0)
return;var table='<table style="font-size:smaller;color:'+options.grid.color+'">'+fragments.join("")+'</table>';if(options.legend.container!=null)
$(options.legend.container).html(table);else{var pos="",p=options.legend.position,m=options.legend.margin;if(m[0]==null)
m=[m,m];if(p.charAt(0)=="n")
pos+='top:'+(m[1]+plotOffset.top)+'px;';else if(p.charAt(0)=="s")
pos+='bottom:'+(m[1]+plotOffset.bottom)+'px;';if(p.charAt(1)=="e")
pos+='right:'+(m[0]+plotOffset.right)+'px;';else if(p.charAt(1)=="w")
pos+='left:'+(m[0]+plotOffset.left)+'px;';var legend=$('<div class="legend">'+table.replace('style="','style="position:absolute;'+pos+';')+'</div>').appendTo(placeholder);if(options.legend.backgroundOpacity!=0.0){var c=options.legend.backgroundColor;if(c==null){c=options.grid.backgroundColor;if(c&&typeof c=="string")
c=$.color.parse(c);else
c=$.color.extract(legend,'background-color');c.a=1;c=c.toString();}
var div=legend.children();$('<div style="position:absolute;width:'+div.width()+'px;height:'+div.height()+'px;'+pos+'background-color:'+c+';"> </div>').prependTo(legend).css('opacity',options.legend.backgroundOpacity);}}}
var highlights=[],redrawTimeout=null;function findNearbyItem(mouseX,mouseY,seriesFilter){var maxDistance=options.grid.mouseActiveRadius,smallestDistance=maxDistance*maxDistance+1,item=null,foundPoint=false,i,j,ps;for(i=series.length-1;i>=0;--i){if(!seriesFilter(series[i]))
continue;var s=series[i],axisx=s.xaxis,axisy=s.yaxis,points=s.datapoints.points,mx=axisx.c2p(mouseX),my=axisy.c2p(mouseY),maxx=maxDistance/axisx.scale,maxy=maxDistance/axisy.scale;ps=s.datapoints.pointsize;if(axisx.options.inverseTransform)
maxx=Number.MAX_VALUE;if(axisy.options.inverseTransform)
maxy=Number.MAX_VALUE;if(s.lines.show||s.points.show){for(j=0;j<points.length;j+=ps){var x=points[j],y=points[j+1];if(x==null)
continue;if(x-mx>maxx||x-mx<-maxx||y-my>maxy||y-my<-maxy)
continue;var dx=Math.abs(axisx.p2c(x)-mouseX),dy=Math.abs(axisy.p2c(y)-mouseY),dist=dx*dx+dy*dy;if(dist<smallestDistance){smallestDistance=dist;item=[i,j/ps];}}}
if(s.bars.show&&!item){var barLeft=s.bars.align=="left"?0:-s.bars.barWidth/2,barRight=barLeft+s.bars.barWidth;for(j=0;j<points.length;j+=ps){var x=points[j],y=points[j+1],b=points[j+2];if(x==null)
continue;if(series[i].bars.horizontal?(mx<=Math.max(b,x)&&mx>=Math.min(b,x)&&my>=y+barLeft&&my<=y+barRight):(mx>=x+barLeft&&mx<=x+barRight&&my>=Math.min(b,y)&&my<=Math.max(b,y)))
item=[i,j/ps];}}}
if(item){i=item[0];j=item[1];ps=series[i].datapoints.pointsize;return{datapoint:series[i].datapoints.points.slice(j*ps,(j+1)*ps),dataIndex:j,series:series[i],seriesIndex:i};}
return null;}
function onMouseMove(e){if(options.grid.hoverable)
triggerClickHoverEvent("plothover",e,function(s){return!!s["hoverable"];});}
function onMouseLeave(e){if(options.grid.hoverable)
triggerClickHoverEvent("plothover",e,function(s){return false;});}
function onClick(e){triggerClickHoverEvent("plotclick",e,function(s){return!!s["clickable"];});}
function triggerClickHoverEvent(eventname,event,seriesFilter){var offset=eventHolder.offset(),canvasX=event.pageX-offset.left-plotOffset.left,canvasY=event.pageY-offset.top-plotOffset.top,pos=canvasToAxisCoords({left:canvasX,top:canvasY});pos.pageX=event.pageX;pos.pageY=event.pageY;var item=findNearbyItem(canvasX,canvasY,seriesFilter);if(item){item.pageX=parseInt(item.series.xaxis.p2c(item.datapoint[0])+offset.left+plotOffset.left,10);item.pageY=parseInt(item.series.yaxis.p2c(item.datapoint[1])+offset.top+plotOffset.top,10);}
if(options.grid.autoHighlight){for(var i=0;i<highlights.length;++i){var h=highlights[i];if(h.auto==eventname&&!(item&&h.series==item.series&&h.point[0]==item.datapoint[0]&&h.point[1]==item.datapoint[1]))
unhighlight(h.series,h.point);}
if(item)
highlight(item.series,item.datapoint,eventname);}
placeholder.trigger(eventname,[pos,item]);}
function triggerRedrawOverlay(){var t=options.interaction.redrawOverlayInterval;if(t==-1){drawOverlay();return;}
if(!redrawTimeout)
redrawTimeout=setTimeout(drawOverlay,t);}
function drawOverlay(){redrawTimeout=null;octx.save();octx.clearRect(0,0,canvasWidth,canvasHeight);octx.translate(plotOffset.left,plotOffset.top);var i,hi;for(i=0;i<highlights.length;++i){hi=highlights[i];if(hi.series.bars.show)
drawBarHighlight(hi.series,hi.point);else
drawPointHighlight(hi.series,hi.point);}
octx.restore();executeHooks(hooks.drawOverlay,[octx]);}
function highlight(s,point,auto){if(typeof s=="number")
s=series[s];if(typeof point=="number"){var ps=s.datapoints.pointsize;point=s.datapoints.points.slice(ps*point,ps*(point+1));}
var i=indexOfHighlight(s,point);if(i==-1){highlights.push({series:s,point:point,auto:auto});triggerRedrawOverlay();}
else if(!auto)
highlights[i].auto=false;}
function unhighlight(s,point){if(s==null&&point==null){highlights=[];triggerRedrawOverlay();}
if(typeof s=="number")
s=series[s];if(typeof point=="number")
point=s.data[point];var i=indexOfHighlight(s,point);if(i!=-1){highlights.splice(i,1);triggerRedrawOverlay();}}
function indexOfHighlight(s,p){for(var i=0;i<highlights.length;++i){var h=highlights[i];if(h.series==s&&h.point[0]==p[0]&&h.point[1]==p[1])
return i;}
return-1;}
function drawPointHighlight(series,point){var x=point[0],y=point[1],axisx=series.xaxis,axisy=series.yaxis,highlightColor=(typeof series.highlightColor==="string")?series.highlightColor:$.color.parse(series.color).scale('a',0.5).toString();if(x<axisx.min||x>axisx.max||y<axisy.min||y>axisy.max)
return;var pointRadius=series.points.radius+series.points.lineWidth/2;octx.lineWidth=pointRadius;octx.strokeStyle=highlightColor;var radius=1.5*pointRadius;x=axisx.p2c(x);y=axisy.p2c(y);octx.beginPath();if(series.points.symbol=="circle")
octx.arc(x,y,radius,0,2*Math.PI,false);else
series.points.symbol(octx,x,y,radius,false);octx.closePath();octx.stroke();}
function drawBarHighlight(series,point){var highlightColor=(typeof series.highlightColor==="string")?series.highlightColor:$.color.parse(series.color).scale('a',0.5).toString(),fillStyle=highlightColor,barLeft=series.bars.align=="left"?0:-series.bars.barWidth/2;octx.lineWidth=series.bars.lineWidth;octx.strokeStyle=highlightColor;drawBar(point[0],point[1],point[2]||0,barLeft,barLeft+series.bars.barWidth,0,function(){return fillStyle;},series.xaxis,series.yaxis,octx,series.bars.horizontal,series.bars.lineWidth);}
function getColorOrGradient(spec,bottom,top,defaultColor){if(typeof spec=="string")
return spec;else{var gradient=ctx.createLinearGradient(0,top,0,bottom);for(var i=0,l=spec.colors.length;i<l;++i){var c=spec.colors[i];if(typeof c!="string"){var co=$.color.parse(defaultColor);if(c.brightness!=null)
co=co.scale('rgb',c.brightness);if(c.opacity!=null)
co.a*=c.opacity;c=co.toString();}
gradient.addColorStop(i/(l-1),c);}
return gradient;}}}
$.plot=function(placeholder,data,options){var plot=new Plot($(placeholder),data,options,$.plot.plugins);return plot;};$.plot.version="0.7";$.plot.plugins=[];function floorInBase(n,base){return base*Math.floor(n/base);}})(jQuery);(function($){var options={xaxis:{categories:null},yaxis:{categories:null}};function processRawData(plot,series,data,datapoints){var xCategories=series.xaxis.options.mode=="categories",yCategories=series.yaxis.options.mode=="categories";if(!(xCategories||yCategories))
return;var format=datapoints.format;if(!format){var s=series;format=[];format.push({x:true,number:true,required:true});format.push({y:true,number:true,required:true});if(s.bars.show||(s.lines.show&&s.lines.fill)){format.push({y:true,number:true,required:false,defaultValue:0});if(s.bars.horizontal){delete format[format.length-1].y;format[format.length-1].x=true;}}
datapoints.format=format;}
for(var m=0;m<format.length;++m){if(format[m].x&&xCategories)
format[m].number=false;if(format[m].y&&yCategories)
format[m].number=false;}}
function getNextIndex(categories){var index=-1;for(var v in categories)
if(categories[v]>index)
index=categories[v];return index+1;}
function categoriesTickGenerator(axis){var res=[];for(var label in axis.categories){var v=axis.categories[label];if(v>=axis.min&&v<=axis.max)
res.push([v,label]);}
res.sort(function(a,b){return a[0]-b[0];});return res;}
function setupCategoriesForAxis(series,axis,datapoints){if(series[axis].options.mode!="categories")
return;if(!series[axis].categories){var c={},o=series[axis].options.categories||{};if($.isArray(o)){for(var i=0;i<o.length;++i)
c[o[i]]=i;}
else{for(var v in o)
c[v]=o[v];}
series[axis].categories=c;}
if(!series[axis].options.ticks)
series[axis].options.ticks=categoriesTickGenerator;transformPointsOnAxis(datapoints,axis,series[axis].categories);}
function transformPointsOnAxis(datapoints,axis,categories){var points=datapoints.points,ps=datapoints.pointsize,format=datapoints.format,formatColumn=axis.charAt(0),index=getNextIndex(categories);for(var i=0;i<points.length;i+=ps){if(points[i]==null)
continue;for(var m=0;m<ps;++m){var val=points[i+m];if(val==null||!format[m][formatColumn])
continue;if(!(val in categories)){categories[val]=index;++index;}
points[i+m]=categories[val];}}}
function processDatapoints(plot,series,datapoints){setupCategoriesForAxis(series,"xaxis",datapoints);setupCategoriesForAxis(series,"yaxis",datapoints);}
function init(plot){plot.hooks.processRawData.push(processRawData);plot.hooks.processDatapoints.push(processDatapoints);}
$.plot.plugins.push({init:init,options:options,name:'categories',version:'1.0'});})(jQuery);(function($){function processRawData(plot,series,datapoints){var handlers={square:function(ctx,x,y,radius,shadow){var size=radius*Math.sqrt(Math.PI)/2;ctx.rect(x-size,y-size,size+size,size+size);},diamond:function(ctx,x,y,radius,shadow){var size=radius*Math.sqrt(Math.PI/2);ctx.moveTo(x-size,y);ctx.lineTo(x,y-size);ctx.lineTo(x+size,y);ctx.lineTo(x,y+size);ctx.lineTo(x-size,y);},triangle:function(ctx,x,y,radius,shadow){var size=radius*Math.sqrt(2*Math.PI/Math.sin(Math.PI/3));var height=size*Math.sin(Math.PI/3);ctx.moveTo(x-size/2,y+height/2);ctx.lineTo(x+size/2,y+height/2);if(!shadow){ctx.lineTo(x,y-height/2);ctx.lineTo(x-size/2,y+height/2);}},cross:function(ctx,x,y,radius,shadow){var size=radius*Math.sqrt(Math.PI)/2;ctx.moveTo(x-size,y-size);ctx.lineTo(x+size,y+size);ctx.moveTo(x-size,y+size);ctx.lineTo(x+size,y-size);}};var s=series.points.symbol;if(handlers[s])
series.points.symbol=handlers[s];}
function init(plot){plot.hooks.processDatapoints.push(processRawData);}
$.plot.plugins.push({init:init,name:'symbols',version:'1.0'});})(jQuery);(function($){var options={crosshair:{mode:null,color:"rgba(170, 0, 0, 0.80)",lineWidth:1}};function init(plot){var crosshair={x:-1,y:-1,locked:false};plot.setCrosshair=function setCrosshair(pos){if(!pos)
crosshair.x=-1;else{var o=plot.p2c(pos);crosshair.x=Math.max(0,Math.min(o.left,plot.width()));crosshair.y=Math.max(0,Math.min(o.top,plot.height()));}
plot.triggerRedrawOverlay();};plot.clearCrosshair=plot.setCrosshair;plot.lockCrosshair=function lockCrosshair(pos){if(pos)
plot.setCrosshair(pos);crosshair.locked=true;};plot.unlockCrosshair=function unlockCrosshair(){crosshair.locked=false;};function onMouseOut(e){if(crosshair.locked)
return;if(crosshair.x!=-1){crosshair.x=-1;plot.triggerRedrawOverlay();}}
function onMouseMove(e){if(crosshair.locked)
return;if(plot.getSelection&&plot.getSelection()){crosshair.x=-1;return;}
var offset=plot.offset();crosshair.x=Math.max(0,Math.min(e.pageX-offset.left,plot.width()));crosshair.y=Math.max(0,Math.min(e.pageY-offset.top,plot.height()));plot.triggerRedrawOverlay();}
plot.hooks.bindEvents.push(function(plot,eventHolder){if(!plot.getOptions().crosshair.mode)
return;eventHolder.mouseout(onMouseOut);eventHolder.mousemove(onMouseMove);});plot.hooks.drawOverlay.push(function(plot,ctx){var c=plot.getOptions().crosshair;if(!c.mode)
return;var plotOffset=plot.getPlotOffset();ctx.save();ctx.translate(plotOffset.left,plotOffset.top);if(crosshair.x!=-1){ctx.strokeStyle=c.color;ctx.lineWidth=c.lineWidth;ctx.lineJoin="round";ctx.beginPath();if(c.mode.indexOf("x")!=-1){ctx.moveTo(crosshair.x,0);ctx.lineTo(crosshair.x,plot.height());}
if(c.mode.indexOf("y")!=-1){ctx.moveTo(0,crosshair.y);ctx.lineTo(plot.width(),crosshair.y);}
ctx.stroke();}
ctx.restore();});plot.hooks.shutdown.push(function(plot,eventHolder){eventHolder.unbind("mouseout",onMouseOut);eventHolder.unbind("mousemove",onMouseMove);});}
$.plot.plugins.push({init:init,options:options,name:'crosshair',version:'1.0'});})(jQuery);(function($){var options={series:{stack:null}};function init(plot){function findMatchingSeries(s,allseries){var res=null;for(var i=0;i<allseries.length;++i){if(s==allseries[i])
break;if(allseries[i].stack==s.stack)
res=allseries[i];}
return res;}
function stackData(plot,s,datapoints){if(s.stack==null)
return;var other=findMatchingSeries(s,plot.getData());if(!other)
return;var ps=datapoints.pointsize,points=datapoints.points,otherps=other.datapoints.pointsize,otherpoints=other.datapoints.points,newpoints=[],px,py,intery,qx,qy,bottom,withlines=s.lines.show,horizontal=s.bars.horizontal,withbottom=ps>2&&(horizontal?datapoints.format[2].x:datapoints.format[2].y),withsteps=withlines&&s.lines.steps,fromgap=true,keyOffset=horizontal?1:0,accumulateOffset=horizontal?0:1,i=0,j=0,l,m;while(true){if(i>=points.length)
break;l=newpoints.length;if(points[i]==null){for(m=0;m<ps;++m)
newpoints.push(points[i+m]);i+=ps;}
else if(j>=otherpoints.length){if(!withlines){for(m=0;m<ps;++m)
newpoints.push(points[i+m]);}
i+=ps;}
else if(otherpoints[j]==null){for(m=0;m<ps;++m)
newpoints.push(null);fromgap=true;j+=otherps;}
else{px=points[i+keyOffset];py=points[i+accumulateOffset];qx=otherpoints[j+keyOffset];qy=otherpoints[j+accumulateOffset];bottom=0;if(px==qx){for(m=0;m<ps;++m)
newpoints.push(points[i+m]);newpoints[l+accumulateOffset]+=qy;bottom=qy;i+=ps;j+=otherps;}
else if(px>qx){if(withlines&&i>0&&points[i-ps]!=null){intery=py+(points[i-ps+accumulateOffset]-py)*(qx-px)/(points[i-ps+keyOffset]-px);newpoints.push(qx);newpoints.push(intery+qy);for(m=2;m<ps;++m)
newpoints.push(points[i+m]);bottom=qy;}
j+=otherps;}
else{if(fromgap&&withlines){i+=ps;continue;}
for(m=0;m<ps;++m)
newpoints.push(points[i+m]);if(withlines&&j>0&&otherpoints[j-otherps]!=null)
bottom=qy+(otherpoints[j-otherps+accumulateOffset]-qy)*(px-qx)/(otherpoints[j-otherps+keyOffset]-qx);newpoints[l+accumulateOffset]+=bottom;i+=ps;}
fromgap=false;if(l!=newpoints.length&&withbottom)
newpoints[l+2]+=bottom;}
if(withsteps&&l!=newpoints.length&&l>0&&newpoints[l]!=null&&newpoints[l]!=newpoints[l-ps]&&newpoints[l+1]!=newpoints[l-ps+1]){for(m=0;m<ps;++m)
newpoints[l+ps+m]=newpoints[l+m];newpoints[l+1]=newpoints[l-ps+1];}}
datapoints.points=newpoints;}
plot.hooks.processDatapoints.push(stackData);}
$.plot.plugins.push({init:init,options:options,name:'stack',version:'1.2'});})(jQuery);(function($){function init(plot){var canvas=null,canvasWidth=0,canvasHeight=0,target=null,maxRadius=null,centerLeft=null,centerTop=null,total=0,redraw=true,redrawAttempts=10,shrink=0.95,legendWidth=0,processed=false,raw=false,ctx=null;var highlights=[];plot.hooks.processOptions.push(checkPieEnabled);plot.hooks.bindEvents.push(bindEvents);function checkPieEnabled(plot,options){if(options.series.pie.show){options.grid.show=false;if(options.series.pie.label.show=="auto"){if(options.legend.show){options.series.pie.label.show=false;}else{options.series.pie.label.show=true;}}
if(options.series.pie.radius=="auto"){if(options.series.pie.label.show){options.series.pie.radius=3/4;}else{options.series.pie.radius=1;}}
if(options.series.pie.tilt>1){options.series.pie.tilt=1;}else if(options.series.pie.tilt<0){options.series.pie.tilt=0;}
plot.hooks.processDatapoints.push(processDatapoints);plot.hooks.drawOverlay.push(drawOverlay);plot.hooks.draw.push(draw);}}
function bindEvents(plot,eventHolder){var options=plot.getOptions();if(options.series.pie.show){if(options.grid.hoverable){eventHolder.unbind("mousemove").mousemove(onMouseMove);}
if(options.grid.clickable){eventHolder.unbind("click").click(onClick);}}}
function alertObject(obj){var msg="";function traverse(obj,depth){if(!depth){depth=0;}
for(var i=0;i<obj.length;++i){for(var j=0;j<depth;j++){msg+="\t";}
if(typeof obj[i]=="object"){msg+=""+i+":\n";traverse(obj[i],depth+1);}else{msg+=""+i+": "+obj[i]+"\n";}}}
traverse(obj);alert(msg);}
function calcTotal(data){for(var i=0;i<data.length;++i){var item=parseFloat(data[i].data[0][1]);if(item){total+=item;}}}
function processDatapoints(plot,series,data,datapoints){if(!processed){processed=true;canvas=plot.getCanvas();target=$(canvas).parent();options=plot.getOptions();canvasWidth=plot.getPlaceholder().width();canvasHeight=plot.getPlaceholder().height();plot.setData(combine(plot.getData()));}}
function setupPie(){legendWidth=target.children().filter(".legend").children().width()||0;maxRadius=Math.min(canvasWidth,canvasHeight/options.series.pie.tilt)/2;centerTop=canvasHeight/2+options.series.pie.offset.top;centerLeft=canvasWidth/2;if(options.series.pie.offset.left=="auto"){if(options.legend.position.match("w")){centerLeft+=legendWidth/2;}else{centerLeft-=legendWidth/2;}}else{centerLeft+=options.series.pie.offset.left;}
if(centerLeft<maxRadius){centerLeft=maxRadius;}else if(centerLeft>canvasWidth-maxRadius){centerLeft=canvasWidth-maxRadius;}}
function fixData(data){for(var i=0;i<data.length;++i){if(typeof(data[i].data)=="number"){data[i].data=[[1,data[i].data]];}else if(typeof(data[i].data)=="undefined"||typeof(data[i].data[0])=="undefined"){if(typeof(data[i].data)!="undefined"&&typeof(data[i].data.label)!="undefined"){data[i].label=data[i].data.label;}
data[i].data=[[1,0]];}}
return data;}
function combine(data){data=fixData(data);calcTotal(data);var combined=0;var numCombined=0;var color=options.series.pie.combine.color;var newdata=[];for(var i=0;i<data.length;++i){data[i].data[0][1]=parseFloat(data[i].data[0][1]);if(!data[i].data[0][1]){data[i].data[0][1]=0;}
if(data[i].data[0][1]/total<=options.series.pie.combine.threshold){combined+=data[i].data[0][1];numCombined++;if(!color){color=data[i].color;}}else{newdata.push({data:[[1,data[i].data[0][1]]],color:data[i].color,label:data[i].label,angle:data[i].data[0][1]*Math.PI*2/total,percent:data[i].data[0][1]/total*100});}}
if(numCombined>0){newdata.push({data:[[1,combined]],color:color,label:options.series.pie.combine.label,angle:combined*Math.PI*2/total,percent:combined/total*100});}
return newdata;}
function draw(plot,newCtx){if(!target){return;}
ctx=newCtx;setupPie();var slices=plot.getData();var attempts=0;while(redraw&&attempts<redrawAttempts){redraw=false;if(attempts>0){maxRadius*=shrink;}
attempts+=1;clear();if(options.series.pie.tilt<=0.8){drawShadow();}
drawPie();}
if(attempts>=redrawAttempts){clear();target.prepend("<div class='error'>Could not draw pie with labels contained inside canvas</div>");}
if(plot.setSeries&&plot.insertLegend){plot.setSeries(slices);plot.insertLegend();}
function clear(){ctx.clearRect(0,0,canvasWidth,canvasHeight);target.children().filter(".pieLabel, .pieLabelBackground").remove();}
function drawShadow(){var shadowLeft=options.series.pie.shadow.left;var shadowTop=options.series.pie.shadow.top;var edge=10;var alpha=options.series.pie.shadow.alpha;var radius=options.series.pie.radius>1?options.series.pie.radius:maxRadius*options.series.pie.radius;if(radius>=canvasWidth/2-shadowLeft||radius*options.series.pie.tilt>=canvasHeight/2-shadowTop||radius<=edge){return;}
ctx.save();ctx.translate(shadowLeft,shadowTop);ctx.globalAlpha=alpha;ctx.fillStyle="#000";ctx.translate(centerLeft,centerTop);ctx.scale(1,options.series.pie.tilt);for(var i=1;i<=edge;i++){ctx.beginPath();ctx.arc(0,0,radius,0,Math.PI*2,false);ctx.fill();radius-=i;}
ctx.restore();}
function drawPie(){var startAngle=Math.PI*options.series.pie.startAngle;var radius=options.series.pie.radius>1?options.series.pie.radius:maxRadius*options.series.pie.radius;ctx.save();ctx.translate(centerLeft,centerTop);ctx.scale(1,options.series.pie.tilt);ctx.save();var currentAngle=startAngle;for(var i=0;i<slices.length;++i){slices[i].startAngle=currentAngle;drawSlice(slices[i].angle,slices[i].color,true);}
ctx.restore();if(options.series.pie.stroke.width>0){ctx.save();ctx.lineWidth=options.series.pie.stroke.width;currentAngle=startAngle;for(var i=0;i<slices.length;++i){drawSlice(slices[i].angle,options.series.pie.stroke.color,false);}
ctx.restore();}
drawDonutHole(ctx);if(options.series.pie.label.show){drawLabels();}
ctx.restore();function drawSlice(angle,color,fill){if(angle<=0||isNaN(angle)){return;}
if(fill){ctx.fillStyle=color;}else{ctx.strokeStyle=color;ctx.lineJoin="round";}
ctx.beginPath();if(Math.abs(angle-Math.PI*2)>0.000000001){ctx.moveTo(0,0);}else if($.browser.msie){angle-=0.0001;}
ctx.arc(0,0,radius,currentAngle,currentAngle+angle/2,false);ctx.arc(0,0,radius,currentAngle+angle/2,currentAngle+angle,false);ctx.closePath();currentAngle+=angle;if(fill){ctx.fill();}else{ctx.stroke();}}
function drawLabels(){var currentAngle=startAngle;var radius=options.series.pie.label.radius>1?options.series.pie.label.radius:maxRadius*options.series.pie.label.radius;for(var i=0;i<slices.length;++i){if(slices[i].percent>=options.series.pie.label.threshold*100){drawLabel(slices[i],currentAngle,i);}
currentAngle+=slices[i].angle;}
function drawLabel(slice,startAngle,index){if(slice.data[0][1]==0){return;}
var lf=options.legend.labelFormatter,text,plf=options.series.pie.label.formatter;if(lf){text=lf(slice.label,slice);}else{text=slice.label;}
if(plf){text=plf(text,slice);}
var halfAngle=((startAngle+slice.angle)+startAngle)/2;var x=centerLeft+Math.round(Math.cos(halfAngle)*radius);var y=centerTop+Math.round(Math.sin(halfAngle)*radius)*options.series.pie.tilt;var html="<span class='pieLabel' id='pieLabel"+index+"' style='position:absolute;top:"+y+"px;left:"+x+"px;'>"+text+"</span>";target.append(html);var label=target.children("#pieLabel"+index);var labelTop=(y-label.height()/2);var labelLeft=(x-label.width()/2);label.css("top",labelTop);label.css("left",labelLeft);if(0-labelTop>0||0-labelLeft>0||canvasHeight-(labelTop+label.height())<0||canvasWidth-(labelLeft+label.width())<0){redraw=true;}
if(options.series.pie.label.background.opacity!=0){var c=options.series.pie.label.background.color;if(c==null){c=slice.color;}
var pos="top:"+labelTop+"px;left:"+labelLeft+"px;";$("<div class='pieLabelBackground' style='position:absolute;width:"+label.width()+"px;height:"+label.height()+"px;"+pos+"background-color:"+c+";'></div>").css("opacity",options.series.pie.label.background.opacity).insertBefore(label);}}}}}
function drawDonutHole(layer){if(options.series.pie.innerRadius>0){layer.save();var innerRadius=options.series.pie.innerRadius>1?options.series.pie.innerRadius:maxRadius*options.series.pie.innerRadius;layer.globalCompositeOperation="destination-out";layer.beginPath();layer.fillStyle=options.series.pie.stroke.color;layer.arc(0,0,innerRadius,0,Math.PI*2,false);layer.fill();layer.closePath();layer.restore();layer.save();layer.beginPath();layer.strokeStyle=options.series.pie.stroke.color;layer.arc(0,0,innerRadius,0,Math.PI*2,false);layer.stroke();layer.closePath();layer.restore();}}
function isPointInPoly(poly,pt){for(var c=false,i=-1,l=poly.length,j=l-1;++i<l;j=i)
((poly[i][1]<=pt[1]&&pt[1]<poly[j][1])||(poly[j][1]<=pt[1]&&pt[1]<poly[i][1]))&&(pt[0]<(poly[j][0]-poly[i][0])*(pt[1]-poly[i][1])/(poly[j][1]-poly[i][1])+poly[i][0])&&(c=!c);return c;}
function findNearbySlice(mouseX,mouseY){var slices=plot.getData(),options=plot.getOptions(),radius=options.series.pie.radius>1?options.series.pie.radius:maxRadius*options.series.pie.radius,x,y;for(var i=0;i<slices.length;++i){var s=slices[i];if(s.pie.show){ctx.save();ctx.beginPath();ctx.moveTo(0,0);ctx.arc(0,0,radius,s.startAngle,s.startAngle+s.angle/2,false);ctx.arc(0,0,radius,s.startAngle+s.angle/2,s.startAngle+s.angle,false);ctx.closePath();x=mouseX-centerLeft;y=mouseY-centerTop;if(ctx.isPointInPath){if(ctx.isPointInPath(mouseX-centerLeft,mouseY-centerTop)){ctx.restore();return{datapoint:[s.percent,s.data],dataIndex:0,series:s,seriesIndex:i};}}else{var p1X=radius*Math.cos(s.startAngle),p1Y=radius*Math.sin(s.startAngle),p2X=radius*Math.cos(s.startAngle+s.angle/4),p2Y=radius*Math.sin(s.startAngle+s.angle/4),p3X=radius*Math.cos(s.startAngle+s.angle/2),p3Y=radius*Math.sin(s.startAngle+s.angle/2),p4X=radius*Math.cos(s.startAngle+s.angle/1.5),p4Y=radius*Math.sin(s.startAngle+s.angle/1.5),p5X=radius*Math.cos(s.startAngle+s.angle),p5Y=radius*Math.sin(s.startAngle+s.angle),arrPoly=[[0,0],[p1X,p1Y],[p2X,p2Y],[p3X,p3Y],[p4X,p4Y],[p5X,p5Y]],arrPoint=[x,y];if(isPointInPoly(arrPoly,arrPoint)){ctx.restore();return{datapoint:[s.percent,s.data],dataIndex:0,series:s,seriesIndex:i};}}
ctx.restore();}}
return null;}
function onMouseMove(e){triggerClickHoverEvent("plothover",e);}
function onClick(e){triggerClickHoverEvent("plotclick",e);}
function triggerClickHoverEvent(eventname,e){var offset=plot.offset();var canvasX=parseInt(e.pageX-offset.left);var canvasY=parseInt(e.pageY-offset.top);var item=findNearbySlice(canvasX,canvasY);if(options.grid.autoHighlight){for(var i=0;i<highlights.length;++i){var h=highlights[i];if(h.auto==eventname&&!(item&&h.series==item.series)){unhighlight(h.series);}}}
if(item){highlight(item.series,eventname);}
var pos={pageX:e.pageX,pageY:e.pageY};target.trigger(eventname,[pos,item]);}
function highlight(s,auto){var i=indexOfHighlight(s);if(i==-1){highlights.push({series:s,auto:auto});plot.triggerRedrawOverlay();}else if(!auto){highlights[i].auto=false;}}
function unhighlight(s){if(s==null){highlights=[];plot.triggerRedrawOverlay();}
var i=indexOfHighlight(s);if(i!=-1){highlights.splice(i,1);plot.triggerRedrawOverlay();}}
function indexOfHighlight(s){for(var i=0;i<highlights.length;++i){var h=highlights[i];if(h.series==s)
return i;}
return-1;}
function drawOverlay(plot,octx){var options=plot.getOptions();var radius=options.series.pie.radius>1?options.series.pie.radius:maxRadius*options.series.pie.radius;octx.save();octx.translate(centerLeft,centerTop);octx.scale(1,options.series.pie.tilt);for(var i=0;i<highlights.length;++i){drawHighlight(highlights[i].series);}
drawDonutHole(octx);octx.restore();function drawHighlight(series){if(series.angle<=0||isNaN(series.angle)){return;}
octx.fillStyle="rgba(255, 255, 255, "+options.series.pie.highlight.opacity+")";octx.beginPath();if(Math.abs(series.angle-Math.PI*2)>0.000000001){octx.moveTo(0,0);}
octx.arc(0,0,radius,series.startAngle,series.startAngle+series.angle/2,false);octx.arc(0,0,radius,series.startAngle+series.angle/2,series.startAngle+series.angle,false);octx.closePath();octx.fill();}}}
var options={series:{pie:{show:false,radius:"auto",innerRadius:0,startAngle:3/2,tilt:1,shadow:{left:5,top:15,alpha:0.02},offset:{top:0,left:"auto"},stroke:{color:"#fff",width:1},label:{show:"auto",formatter:function(label,slice){return"<div style='font-size:x-small;text-align:center;padding:2px;color:"+slice.color+";'>"+label+"<br/>"+Math.round(slice.percent)+"%</div>";},radius:1,background:{color:null,opacity:0},threshold:0},combine:{threshold:-1,color:null,label:"Other"},highlight:{opacity:0.5}}}};$.plot.plugins.push({init:init,options:options,name:"pie",version:"1.1"});})(jQuery);(function($){var options={};function floorInBase(n,base){return base*Math.floor(n/base);}
function formatDate(d,fmt,monthNames,dayNames){if(typeof d.strftime=="function"){return d.strftime(fmt);}
var leftPad=function(n,pad){n=""+n;pad=""+(pad==null?"0":pad);return n.length==1?pad+n:n;};var r=[];var escape=false;var hours=d.getHours();var isAM=hours<12;if(monthNames==null){monthNames=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];}
if(dayNames==null){dayNames=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];}
var hours12;if(hours>12){hours12=hours-12;}else if(hours==0){hours12=12;}else{hours12=hours;}
for(var i=0;i<fmt.length;++i){var c=fmt.charAt(i);if(escape){switch(c){case'a':c=""+dayNames[d.getDay()];break;case'b':c=""+monthNames[d.getMonth()];break;case'd':c=leftPad(d.getDate());break;case'e':c=leftPad(d.getDate()," ");break;case'H':c=leftPad(hours);break;case'I':c=leftPad(hours12);break;case'l':c=leftPad(hours12," ");break;case'm':c=leftPad(d.getMonth()+1);break;case'M':c=leftPad(d.getMinutes());break;case'S':c=leftPad(d.getSeconds());break;case'y':c=leftPad(d.getFullYear()%100);break;case'Y':c=""+d.getFullYear();break;case'p':c=(isAM)?(""+"am"):(""+"pm");break;case'P':c=(isAM)?(""+"AM"):(""+"PM");break;case'w':c=""+d.getDay();break;}
r.push(c);escape=false;}else{if(c=="%"){escape=true;}else{r.push(c);}}}
return r.join("");}
function makeUtcWrapper(d){function addProxyMethod(sourceObj,sourceMethod,targetObj,targetMethod){sourceObj[sourceMethod]=function(){return targetObj[targetMethod].apply(targetObj,arguments);};};var utc={date:d};if(d.strftime!=undefined){addProxyMethod(utc,"strftime",d,"strftime");}
addProxyMethod(utc,"getTime",d,"getTime");addProxyMethod(utc,"setTime",d,"setTime");var props=["Date","Day","FullYear","Hours","Milliseconds","Minutes","Month","Seconds"];for(var p=0;p<props.length;p++){addProxyMethod(utc,"get"+props[p],d,"getUTC"+props[p]);addProxyMethod(utc,"set"+props[p],d,"setUTC"+props[p]);}
return utc;};function dateGenerator(ts,opts){if(opts.timezone=="browser"){return new Date(ts);}else if(!opts.timezone||opts.timezone=="utc"){return makeUtcWrapper(new Date(ts));}else if(typeof timezoneJS!="undefined"&&typeof timezoneJS.Date!="undefined"){var d=new timezoneJS.Date();d.setTimezone(opts.timezone);d.setTime(ts);return d;}else{return makeUtcWrapper(new Date(ts));}}
var timeUnitSize={"second":1000,"minute":60*1000,"hour":60*60*1000,"day":24*60*60*1000,"month":30*24*60*60*1000,"year":365.2425*24*60*60*1000};var spec=[[1,"second"],[2,"second"],[5,"second"],[10,"second"],[30,"second"],[1,"minute"],[2,"minute"],[5,"minute"],[10,"minute"],[30,"minute"],[1,"hour"],[2,"hour"],[4,"hour"],[8,"hour"],[12,"hour"],[1,"day"],[2,"day"],[3,"day"],[0.25,"month"],[0.5,"month"],[1,"month"],[2,"month"],[3,"month"],[6,"month"],[1,"year"]];function init(plot){plot.hooks.processDatapoints.push(function(plot,series,datapoints){$.each(plot.getAxes(),function(axisName,axis){var opts=axis.options;if(opts.mode=="time"){axis.tickGenerator=function(axis){var ticks=[];var d=dateGenerator(axis.min,opts);var minSize=0;if(opts.minTickSize!=null){if(typeof opts.tickSize=="number"){minSize=opts.tickSize;}else{minSize=opts.minTickSize[0]*timeUnitSize[opts.minTickSize[1]];}}
for(var i=0;i<spec.length-1;++i){if(axis.delta<(spec[i][0]*timeUnitSize[spec[i][1]]
+spec[i+1][0]*timeUnitSize[spec[i+1][1]])/2&&spec[i][0]*timeUnitSize[spec[i][1]]>=minSize){break;}}
var size=spec[i][0];var unit=spec[i][1];if(unit=="year"){if(opts.minTickSize!=null&&opts.minTickSize[1]=="year"){size=Math.floor(opts.minTickSize[0]);}else{var magn=Math.pow(10,Math.floor(Math.log(axis.delta/timeUnitSize.year)/Math.LN10));var norm=(axis.delta/timeUnitSize.year)/magn;if(norm<1.5){size=1;}else if(norm<3){size=2;}else if(norm<7.5){size=5;}else{size=10;}
size*=magn;}
if(size<1){size=1;}}
axis.tickSize=opts.tickSize||[size,unit];var tickSize=axis.tickSize[0];unit=axis.tickSize[1];var step=tickSize*timeUnitSize[unit];if(unit=="second"){d.setSeconds(floorInBase(d.getSeconds(),tickSize));}else if(unit=="minute"){d.setMinutes(floorInBase(d.getMinutes(),tickSize));}else if(unit=="hour"){d.setHours(floorInBase(d.getHours(),tickSize));}else if(unit=="month"){d.setMonth(floorInBase(d.getMonth(),tickSize));}else if(unit=="year"){d.setFullYear(floorInBase(d.getFullYear(),tickSize));}
d.setMilliseconds(0);if(step>=timeUnitSize.minute){d.setSeconds(0);}else if(step>=timeUnitSize.hour){d.setMinutes(0);}else if(step>=timeUnitSize.day){d.setHours(0);}else if(step>=timeUnitSize.day*4){d.setDate(1);}else if(step>=timeUnitSize.year){d.setMonth(0);}
var carry=0;var v=Number.NaN;var prev;do{prev=v;v=d.getTime();ticks.push(v);if(unit=="month"){if(tickSize<1){d.setDate(1);var start=d.getTime();d.setMonth(d.getMonth()+1);var end=d.getTime();d.setTime(v+carry*timeUnitSize.hour+(end-start)*tickSize);carry=d.getHours();d.setHours(0);}else{d.setMonth(d.getMonth()+tickSize);}}else if(unit=="year"){d.setFullYear(d.getFullYear()+tickSize);}else{d.setTime(v+step);}}while(v<axis.max&&v!=prev);return ticks;};axis.tickFormatter=function(v,axis){var d=dateGenerator(v,axis.options);if(opts.timeformat!=null){return formatDate(d,opts.timeformat,opts.monthNames,opts.dayNames);}
var t=axis.tickSize[0]*timeUnitSize[axis.tickSize[1]];var span=axis.max-axis.min;var suffix=(opts.twelveHourClock)?" %p":"";var hourCode=(opts.twelveHourClock)?"%I":"%H";var fmt;if(t<timeUnitSize.minute){fmt=hourCode+":%M:%S"+suffix;}else if(t<timeUnitSize.day){if(span<2*timeUnitSize.day){fmt=hourCode+":%M"+suffix;}else{fmt="%b %d "+hourCode+":%M"+suffix;}}else if(t<timeUnitSize.month){fmt="%b %d";}else if(t<timeUnitSize.year){if(span<timeUnitSize.year){fmt="%b";}else{fmt="%b %Y";}}else{fmt="%Y";}
var rt=formatDate(d,fmt,opts.monthNames,opts.dayNames);return rt;};}});});}
$.plot.plugins.push({init:init,options:options,name:'time',version:'1.0'});$.plot.formatDate=formatDate;})(jQuery);(function($,h,c){var a=$([]),e=$.resize=$.extend($.resize,{}),i,k="setTimeout",j="resize",d=j+"-special-event",b="delay",f="throttleWindow";e[b]=250;e[f]=true;$.event.special[j]={setup:function(){if(!e[f]&&this[k]){return false}var l=$(this);a=a.add(l);$.data(this,d,{w:l.width(),h:l.height()});if(a.length===1){g()}},teardown:function(){if(!e[f]&&this[k]){return false}var l=$(this);a=a.not(l);l.removeData(d);if(!a.length){clearTimeout(i)}},add:function(l){if(!e[f]&&this[k]){return false}var n;function m(s,o,p){var q=$(this),r=$.data(this,d);r.w=o!==c?o:q.width();r.h=p!==c?p:q.height();n.apply(this,arguments)}if($.isFunction(l)){n=l;return m}else{n=l.handler;l.handler=m}}};function g(){i=h[k](function(){a.each(function(){var n=$(this),m=n.width(),l=n.height(),o=$.data(this,d);if(m!==o.w||l!==o.h){n.trigger(j,[o.w=m,o.h=l])}});g()},e[b])}})(jQuery,this);(function($){var options={};function init(plot){function onResize(){var placeholder=plot.getPlaceholder();if(placeholder.width()==0||placeholder.height()==0)
return;plot.resize();plot.setupGrid();plot.draw();}
function bindEvents(plot,eventHolder){plot.getPlaceholder().resize(onResize);}
function shutdown(plot,eventHolder){plot.getPlaceholder().unbind("resize",onResize);}
plot.hooks.bindEvents.push(bindEvents);plot.hooks.shutdown.push(shutdown);}
$.plot.plugins.push({init:init,options:options,name:'resize',version:'1.0'});})(jQuery);var opts={lines:13,length:20,width:10,radius:30,corners:0.7,rotate:0,direction:1,color:'#000',speed:1.2,trail:60,shadow:false,hwaccel:false,className:'spinner',zIndex:2e9,top:'auto',left:'auto'};var target=document.getElementById("schedule")
var spinner;var oevent;var hasOwnProperty=Object.prototype.hasOwnProperty;function is_empty(obj){if(obj==null)return true;if(obj.length&&obj.length>0)return false;if(obj.length===0)return true;for(var key in obj){if(hasOwnProperty.call(obj,key))return false;}
return true;}
function EventosActualiza(data)
{if(!is_empty(data))
{oevent.end=data[0].end;oevent.title=data[0].title;oevent.start=data[0].start;oevent.color=data[0].color;oevent.textcolor=data[0].textcolor;oevent.data.pk=data[0].data.pk;oevent.data.accion=data[0].data.accion;oevent.data.detreg=data[0].data.detreg;$('#schedule').fullCalendar('updateEvent',oevent)}}
function Arbol(data)
{$('#arbol').tree({data:data,autoEscape:false});}
var ajax;function onDataReceived(series){if(!alreadyFetched[series.label]){$.each(series,function(i,v){alreadyFetched[series.label]=true;data_ajax.push(series[i]);});}
$.plot(ajax,data_ajax,options_ajax);}
$(document).ready(function(){spineer=new Spinner(opts).spin(target);$("#butregimpresion").click(function(){Dajaxice.appcc.JsonImpRegPanel(Arbol);$('#impregModal').modal('toggle').css({'width':'500px','margin-left':function(){return-($(this).width()/1.5);}})});$("#btnmostrar").click(function(){ajax=$("#grafica"),data_ajax=[],alreadyFetched={},options_ajax={series:{lines:{show:true},points:{show:true},hoverable:true},xaxis:{mode:"time",timeformat:"%d-%m-%y",minTickSize:[1,"day"]},grid:{backgroundColor:'#FFFFFF',borderWidth:1,borderColor:'#D7D7D7',hoverable:true,clickable:true}};$.plot(ajax,data_ajax,options_ajax);var idcab=$('#id_selcabreg').val();Dajaxice.appcc.graficaregistros(onDataReceived,{'idcab':idcab});return false;});$("#closegrafico").click(function()
{})
$("#butreggraficareg").click(function(){Dajaxice.appcc.graficaentrada(Dajax.process)});$("#butreggraficasensor").click(function(){window.open("/grafsensores/");});$("#myModal").on('shown',function(){$(this).find("[autofocus]:first").focus();});$('#myModal').keypress(function(event)
{if(event.keyCode==13)
{$('#id_guardar').click();}});$('#id_guardar').click(function(){Dajaxice.appcc.registrosRapidosGuardar(Dajax.process,{'form':$('#form_registro').serialize(true),'pk':$('#id_registros-id').val().toString(),'detregid':$('#id_registros-detreg_id').val().toString(),'incidencia':'N'});})
$('#id_incidencia').click(function(){Dajaxice.appcc.registrosRapidosGuardar(Dajax.process,{'form':$('#form_registro').serialize(true),'pk':$('#id_registros-id').val().toString(),'detregid':$('#id_registros-detreg_id').val().toString(),'incidencia':'S'});});$('[data-form=datepicker]').datepicker({format:'dd/mm/yyyy',language:'es'});var date=new Date();var d=date.getDate();var m=date.getMonth();var y=date.getFullYear();var Es_es={monthNames:['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],monthNamesShort:['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'],dayNames:['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sabado'],dayNamesShort:['Dom','Lun','Mar','Mié','Jue','Vie','Sab'],buttonText:{prev:'&nbsp;&#9668;&nbsp;',next:'&nbsp;&#9658;&nbsp;',prevYear:'&nbsp;&lt;&lt;&nbsp;',nextYear:'&nbsp;&gt;&gt;&nbsp;',today:'hoy',month:'mes',week:'semana',day:'dia'},titleFormat:{month:'MMMM yyyy',week:"d [ yyyy]{ '&#8212;'[ MMM] d MMM yyyy}",day:'dddd, d MMM, yyyy'},columnFormat:{month:'ddd',week:'ddd d/M',day:'dddd d/M'},allDayText:'día todo',axisFormat:'H:mm',timeFormat:{'':'H(:mm)',agenda:'H:mm{ - H:mm}'}}
$.fullCalendar.setDefaults(Es_es)
function Eventos(data)
{spineer.stop();var calendar=$('#schedule').fullCalendar({defaultView:'basicDay',eventClick:function(event){if(event.data.accion.indexOf('E')==-1)
{oevent=event;pk=event.data.pk;sfecha=event.data.fecha;Dajaxice.appcc.registrosRapidosNuevo(Dajax.process,{'pk':pk,'sfecha':sfecha});return false;}
else
{oevent=event;pk=event.data.pk;detreg=event.data.detreg
Dajaxice.appcc.registrosRapidosEditar(Dajax.process,{'pk':pk,'detregid':detreg});return false;}
$(this).css('border-color','red');},header:{left:'title',center:'',right:'prev,next today,month,basicWeek,basicDay'},events:data});}
Dajaxice.appcc.eventos(Eventos);});