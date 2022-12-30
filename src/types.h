/* -*- Mode: C; tab-width: 8; indent-tabs-mode: nil; c-basic-offset: 8 -*-
 *
 * Copyright (C) 2009-2010 Red Hat, Inc.
 * Copyright (c) 2023 Serenity Cybersecurity, LLC <license@futurecrew.ru>
 *               Author: Gleb Popov <arrowd@FreeBSD.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 * Written by: Matthias Clasen <mclasen@redhat.com>
 */

#pragma once

#include "config.h"

typedef struct Daemon Daemon;
typedef struct User User;

/* compatibility shim just to make the code compile */
#ifndef HAVE_SHADOW_H
struct spwd
{
        char             *sp_namp;
        char             *sp_pwdp;
        long int          sp_lstchg;
        long int          sp_min;
        long int          sp_max;
        long int          sp_warn;
        long int          sp_inact;
        long int          sp_expire;
        unsigned long int sp_flag;
};
#endif
