/**
 * Javascript-Equal-Height-Responsive-Rows
 * https://github.com/Sam152/Javascript-Equal-Height-Responsive-Rows
 */
(function($) {
  'use strict';

    /**
     * Set all elements within the collection to have the same height.
     */
    $.fn.equalHeight = function() {
        var heights = [];
        $.each(this, function(i, element) {
            var $element = $(element);
            
			//alert($element.parents('col-lg-4').length);
			//if ($element.parents('col-lg-4').length>0)
			{
				var elementHeight;
				// Should we include the elements padding in it's height?
				var includePadding = ($element.css('box-sizing') === 'border-box') || ($element.css('-moz-box-sizing') === 'border-box');
				if (includePadding) {
					elementHeight = $element.innerHeight();
				} else {
					elementHeight = $element.height();
				}
				
				//alert($element.height());
				
				//alert($element.attr('data-widgster-collapsed'));
				
				//if (!($element.attr('data-widgster-collapsed')))
				//if ()
				heights.push(elementHeight);
			}
        });
        $.each(this, function(i, element) {
            var $element = $(element);
            
			//alert($element.parents('col-lg-4').length);
			//if ($element.parents('col-lg-4').length>0)
			{
				var elementHeight;
				// Should we include the elements padding in it's height?
				var includePadding = ($element.css('box-sizing') === 'border-box') || ($element.css('-moz-box-sizing') === 'border-box');
				if (includePadding) {
					elementHeight = $element.innerHeight();
				} else {
					elementHeight = $element.height();
				}
				
				//alert($element.height());
				
				//alert($element.attr('data-widgster-collapsed'));
				
				if ($element.height()>30)
					$element.css('height', Math.max.apply(window, heights) + 'px');
			}
        });
        //this.filter(function(index) { if (this[index].height()<40) return false; return true; })
        return this;
    };

    /**
     * Create a grid of equal height elements.
     */
    $.fn.equalHeightGrid = function(columns) {
        var $tiles = this.filter(':visible');
        $tiles.css('height', 'auto');
        for (var i = 0; i < $tiles.length; i++) {
            if (i % columns === 0) {
                var row = $($tiles[i]);
                for (var n = 1; n < columns; n++) {
                    row = row.add($tiles[i + n]);
                }
                row.equalHeight();
            }
        }
        return this;
    };

    /**
     * Detect how many columns there are in a given layout.
     */
    $.fn.detectGridColumns = function() {
        var offset = 0,
            cols = 0,
            $tiles = this.filter(':visible');
        $tiles.each(function(i, elem) {
            var elemOffset = $(elem).offset().top;
            if (offset === 0 || elemOffset === offset) {
                cols++;
                offset = elemOffset;
            } else {
                return false;
            }
        });
        return cols;
    };

    /**
     * Ensure equal heights now, on ready, load and resize.
     */
    var grids_event_uid = 0;
    $.fn.responsiveEqualHeightGrid = function() {
        var _this = this;
        var event_namespace = '.grids_' + grids_event_uid;
        _this.data('grids-event-namespace', event_namespace);
        function syncHeights() {
            var cols = _this.detectGridColumns();
            _this.equalHeightGrid(cols);
        }
        $(window).bind('resize' + event_namespace + ' load' + event_namespace, syncHeights);
        syncHeights();
        grids_event_uid++;
        return this;
    };

    /**
     * Unbind created events for a set of elements.
     */
    $.fn.responsiveEqualHeightGridDestroy = function() {
        var _this = this;
        _this.css('height', 'auto');
        $(window).unbind(_this.data('grids-event-namespace'));
        return this;
    };

})(window.jQuery);
