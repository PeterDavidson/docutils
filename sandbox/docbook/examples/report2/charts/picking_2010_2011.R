rates <- read.csv("../tables/all.csv")
x = rates$week
title=''
y1 = rates$rate.picking.2010
y2 = rates$rate.picking.2011
png(file="picking_rate_2010_2011.png", width=5, height=3.5, units="in", res=res )
xlab.text="week in year"
xlab = xlab.text
ylab = "units/man hour"
if (make.title == T ) top.margin = 3
if (make.title != T ) title="" 
if (months.grid == T) bottom.margin = 6
if (months.grid == T) xlab = ''
margins=c(bottom.margin, 4, top.margin, 0.5) 
par(mar=margins) 
par('family'='serif')
y_range = range(y1,y2, na.rm=T)
plot(x, type='n', xlab=xlab, ylab=ylab, las=1,
main=title, ylim=y_range, axes=F, mgp=c(2.5,1,0))
axis(1, col=ax_col)
axis(2, col=ax_col, las=1, at=axTicks(2))
box(col=box_col)
abline( h=axTicks(2), lty=1, lwd=lwd_grid, col=ax_col)
lines(x,y1, col=line_colors[1],  lwd=lwd, lty=line_types[1])
lines(x, y2, col=line_colors[2],  lwd=lwd, lty=line_types[2])
legend("bottomleft", c("2010", "2011"), cex=legend_font_size, 
 col=line_colors,  lty=line_types, bty='y', box.lwd=box.lwd)
source("make_x_axis.R")
dev.off()

