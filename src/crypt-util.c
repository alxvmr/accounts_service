/* -*- Mode: C; tab-width: 8; indent-tabs-mode: nil; c-basic-offset: 8 -*-
 *
 * Copyright (C) 2004-2005 James M. Cape <jcape@ignore-your.tv>.
 * Copyright (C) 2007-2008 William Jon McCann <mccann@jhu.edu>
 * Copyright (c) 2023 GNOME Foundation Inc.
 *               Contributor: Adrian Vovk
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include "config.h"

#include <glib.h>

#ifdef HAVE_CRYPT_H
#include <crypt.h>
#endif

#include "crypt-util.h"

#ifdef HAVE_CRYPT_GENSALT
static gchar *
generate_salt_for_crypt_hash (void)
{
        return g_strdup (crypt_gensalt (NULL, 0, NULL, 0));
}
#else
static const gchar
salt_char (GRand *rand)
{
        const gchar salt[] = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
                             "abcdefghijklmnopqrstuvxyz"
                             "./0123456789";

        return salt[g_rand_int_range (rand, 0, G_N_ELEMENTS (salt))];
}

static gchar *
generate_salt_for_crypt_hash (void)
{
        g_autoptr (GString) salt = NULL;
        g_autoptr (GRand) rand = NULL;
        gint i;

        rand = g_rand_new ();
        salt = g_string_sized_new (21);

        /* sha512crypt */
        g_string_append (salt, "$6$");
        for (i = 0; i < 16; i++) {
                g_string_append_c (salt, salt_char (rand));
        }
        g_string_append_c (salt, '$');

        return g_strdup (salt->str);
}
#endif

gchar *
hash_password (const gchar *plain)
{
        g_autofree char *salt = NULL;

        salt = generate_salt_for_crypt_hash ();
        return g_strdup (crypt (plain, salt));
}
