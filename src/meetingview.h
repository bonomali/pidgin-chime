/*
 * Copyright © 2020 Amazon.com, Inc. or its affiliates.
 *
 * Authors: Ignacio Casal Quinteiro <icq@gnome.org>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public License
 * version 2.1, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 */

#ifndef CHIME_MEETING_VIEW_H
#define CHIME_MEETING_VIEW_H

#include <gtk/gtk.h>

#include "chime-contact.h"
#include "chime-conversation.h"
#include "chime-room.h"
#include "chime-meeting.h"

G_BEGIN_DECLS

#define CHIME_TYPE_MEETING_VIEW (chime_meeting_view_get_type ())
G_DECLARE_FINAL_TYPE(ChimeMeetingView, chime_meeting_view, CHIME, MEETING_VIEW, GtkGrid)

GtkWidget *chime_meeting_view_new            (void);

void       chime_meeting_view_set_meeting    (ChimeMeetingView *self,
                                              ChimeConnection  *connection,
                                              ChimeMeeting     *meeting);

G_END_DECLS

#endif /* CHIME_MEETING_VIEW_H */

/* ex:set ts=4 et: */
