import gi
import cairo
import time
from random import randint

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk

class Meter(Gtk.DrawingArea):
    def __init__(self):
        super().__init__()
        
        self.width = 0
        self.height = 0
        
        # Cache the background so it does not need to be drawn every time the value changes
        self.cache_surface = None
        
        # Handle connections
        self.connect("draw", self.draw)
        self.connect("size-allocate", self.on_size_allocate)
        
    def on_size_allocate(self,widget,allocation):
        self.width = float(allocation.width)
        self.height = float(allocation.height)
        self.font_size = 10
        
    def draw_background(self, cairo_ctx):
        if not self.cache_surface:
            # Draw new surface
            self.cache_surface = cairo.Surface.create_similar(cairo_ctx.get_target(), cairo.CONTENT_COLOR, int(self.width),int(self.height))
            
            # Create a new context for the cache surface
            cache_cairo_ctx = cairo.Context(self.cache_surface)
            
            cache_cairo_ctx.set_source_rgba(0,0,0,0)
            cache_cairo_ctx.rectangle(0,0,self.width,self.height)
            cache_cairo_ctx.fill()
            
        # Load the cached surface
        cairo_ctx.set_source_surface(self.cache_surface, 0, 0)
        cairo_ctx.paint()
        
    def draw_value(self, cairo_ctx, value, x, width):
        height = self.height
        
        # Create a gradient for the background
        gradient = cairo.LinearGradient(1,1,width - 1, height - 1)
        
        gradient.add_color_stop_rgb(0,1,0,0) # Red at the top
        gradient.add_color_stop_rgb(0.2,1,1,0) # Orange near the top
        gradient.add_color_stop_rgb(1,0,1,0) # Green to the bottom
        
        cairo_ctx.set_source(gradient)
        cairo_ctx.rectangle(x,height * (1 - value), width, height * value)
        cairo_ctx.fill()
        
    def re_draw(self):
        self.queue_draw_area(0,0,int(self.width),int(self.height))
        

class MonoMeter(Meter):
    def __init__(self):
        super().__init__()
        
        self.value = 0.0
        
    def draw(self,widget,cairo_ctx):
        self.draw_background(cairo_ctx)
        
        width = self.width / 4
        x = (self.width - width) / 2
        
        self.draw_value(cairo_ctx,self.value,x,width)
        
    def set_value(self,value):
        self.value = value
        self.re_draw()
        
class StereoMeter(Meter):
    def __init__(self):
        super().__init__()
        
        self.l_value = 0.0
        self.r_value = 0.0
        
    def draw(self,widget,cairo_ctx):
        self.draw_background(cairo_ctx)
        
        width = self.width / 5
        l_x = width
        r_x = width * 3
        
        self.draw_value(cairo_ctx,self.l_value,l_x,width)
        self.draw_value(cairo_ctx,self.r_value,r_x,width)
        
    def set_values(self,left,right):
        self.l_value = left
        self.r_value = right
        self.re_draw()
            