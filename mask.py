import cfg
import dev
import pbs
import tip
import tap
import ohm
import dc
import y1x2
import y2x2
import y4x4


def layouts(x, y):
  _, y = dev.sline(x, y, cfg.lchip)
  _, y = tip.chips(x, y)
  _, y = dev.sline(x, y, cfg.lchip)
  _, y = tip.refer(x, y + cfg.ch)
  _, y = y1x2.chips(x, y + cfg.ch * 0.5)
  _, y = dev.sline(x, y - cfg.ch * 0.5, cfg.lchip)
  _, y = tip.refer(x, y + cfg.ch)
  _, y = y2x2.chips(x, y)
  _, y = dev.sline(x, y - cfg.ch * 0.5, cfg.lchip)
  _, y = tip.refer(x, y + cfg.ch)
  _, y = dc.chips(x, y)
  _, y = dev.sline(x, y, cfg.lchip)
  _, y = tip.refer(x, y + cfg.ch)
  _, y = tap.chips(x, y + cfg.ch)
  _, y = dev.sline(x, y, cfg.lchip)
  _, y = tip.refer(x, y + cfg.ch)
  _, y = ohm.chips(x, y)
  _, y = dev.sline(x, y, cfg.lchip)
  _, y = tip.refer(x, y + cfg.ch)
  _, y = pbs.chips(x, y)
  _, y = dev.sline(x, y, cfg.lchip)
  _, y = tip.refer(x, y + cfg.ch)
  _, y = y4x4.chips(x, y)


if __name__ == '__main__':
  cfg.draft = 'draft'
  layouts(0, 0)
  dev.saveas('draft')
