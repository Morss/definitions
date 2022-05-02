import datetime;

class Definition:
  def __init__(self, recordId, title, tags, people, date, comment, links, area, superceded_by):
    self.recordId = recordId
    self.title = title
    self.tags = tags
    self.people = people
    self.date = date
    self.comment = comment
    self.links = links
    self.area = area
    self.superceded_by = superceded_by