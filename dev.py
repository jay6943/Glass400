import cfg
import dxf
import elr
import cir
import gds


def srect(x, y, length, width):
  return dxf.srect('core', x, y, length, width)


def sline(x, y, length):
  return dxf.srect('core', x, y, length, cfg.wg)


def tline(x, y, length):
  w, dy = cfg.wg * 0.5, y + length
  dxf.crect('core', x - w, y, x + w, dy)
  return x, dy


def tilts(x, y, length, wg, angle):
  return dxf.tilts('core', x, y, length, wg, angle)


def taper(x, y, length, wstart, wstop):
  return dxf.taper('core', x, y, length, wstart, wstop)


def bends(x, y, angle, rotate, xsign, ysign):
  df = elr.curve(cfg.wg, cfg.radius, angle, cfg.draft)
  return dxf.bends('core', df, x, y, rotate, xsign, ysign)


def sbend(x, y, angle, dy):
  df = elr.curve(cfg.wg, cfg.radius, angle, cfg.draft)
  return dxf.sbend('core', df, x, y, dy)


def texts(x, y, title, scale, align):
  xs = {'r': -1, 'l': 1, 'c':1}
  ys = {'t': -50, 'b': 50, 'c':0}
  xsign = xs[align[0]]
  d = 10 * scale * 2  # 10 when scale = 0.5
  dx, _ = dxf.texts('core', x + xsign * d, y, title, scale, align)
  x = x - dx * 0.5 if 'c' in align[0] else x


def marks(layer, x, y, xsize, ysize):
  dl = 150
  dxf.triangle(layer, x, y, x + dl, y, x, y + dl)
  dx = x + xsize
  dxf.triangle(layer, dx, y, dx - dl, y, dx, y + dl)
  dy = y + ysize
  dxf.triangle(layer, x, dy, x + dl, dy, x, dy - dl)
  dxf.triangle(layer, dx, dy, dx - dl, dy, dx, dy - dl)


def split(layer, xpos, ypos):
  dxf.split(layer, xpos * cfg.skey, ypos * cfg.skey)


def euler(wg, radius, angle):
  return elr.curve(wg, radius, angle, cfg.draft)


def circular(wg, radius, angle):
  return cir.curve(wg, radius, angle, cfg.draft)


def savedxf(filename):
  print(f'Saving ... {filename}.dxf')
  dxf.saveas(f'{cfg.path}/{filename}')


def saveas(filename):
  print(f'Saving ... {filename}.gds')
  gds.saveas(f'{cfg.path}/{filename}', cfg.labels)


def dlayers(filename, label1, label2):
  print(f'Writing a difference(#{label1} - #{label2}) on #{label2}')
  gds.dlayers(f'{cfg.path}/{filename}', cfg.labels, label1, label2)


def gdstext(filename):
  print('Inserting text')
  gds.texts(f'{cfg.path}/{filename}', cfg.labels, 11000, 0)
